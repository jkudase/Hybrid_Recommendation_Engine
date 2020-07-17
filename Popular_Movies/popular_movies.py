from Main_Start import  menu
import time
import operator
from itertools import islice, compress,filterfalse
from collections import namedtuple, defaultdict
#from set import Set
import itertools
from tkinter import *

all_genres = ['unknown', 'Action', 'Adventure', 'Animation', 'Children', 
    'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
    'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller',
    'War', 'Western']

def _parse_movies(movie_file):
    movie_attrs = ['id', 'name', 'release_date', 'unknown_field', 'imdb_url']
    movies = {}
    for line in movie_file:
        tokens = line.split('|')
        if not tokens or len(tokens) < 3:
            continue
        
        movie = dict(zip(movie_attrs, tokens))
        genre_bools = map(int, tokens[len(movie_attrs) : len(tokens)])
        genres = set(compress(all_genres, genre_bools))
        movie['genres'] = genres
        movie['release_date'] = coerce_date(movie['release_date'])
        movie['number_of_ratings'] = 0
        movie['sum_of_ratings'] = 0
        
        id = movie['id'] = int(movie['id'])
        movies[id] = movie
    
    return movies

def coerce_date(date_as_str):
    date_as_str = date_as_str.strip()
    if date_as_str:
        return time.strptime(date_as_str, '%d-%b-%Y')
    else:
        return None

Rating = namedtuple('Rating', ['userid', 'movieid', 'rating', 'timestamp'])
def _ratings_iterator(ratings_file):
    for line in ratings_file:
        tokens = line.split()
        if not tokens:
            continue
        tokens = map(int, tokens)
        rating = Rating(*tokens)
        yield rating

def get_movies(movie_file, ratings_file):
    movies = _parse_movies(movie_file)
    ratings = _ratings_iterator(ratings_file)
    ratings_for_valid_movies = filter(lambda x : x.movieid in movies, ratings)

    for rating in ratings_for_valid_movies:
        movies[rating.movieid]['sum_of_ratings'] += rating.rating
        movies[rating.movieid]['number_of_ratings'] += 1
    
    return movies

def most_watched_movie(movies):
    return max(movies, key=(lambda m : m['number_of_ratings']))

def most_watched_genre(movies):
    by_genre = defaultdict(int)
    for movie in movies:
        for genre in movie['genres']:
            by_genre[genre] += movie['number_of_ratings']
    
   # ik = iter(by_genre.keys())
   # return max(by_genre.iterkeys(), key=(lambda genre : by_genre[genre]))
    return max(iter(by_genre.keys()), key=(lambda genre : by_genre[genre]))
    
def most_popular_movie(movies):
    return max(movies, key=(lambda m : m['sum_of_ratings']))

def most_popular_movie_for_genre(movies, genre):
    movies_in_genre = filter(lambda m : genre in m['genres'], movies)
    return most_popular_movie(movies_in_genre)

def most_popular_movie_for_genre_and_year(movies, genre, year):
    movies_with_release_date = filter(lambda m : operator.truth(m['release_date']), movies)
    movies_in_year = filter(lambda m : m['release_date'].tm_year == year, movies_with_release_date)
    movies_in_year_in_genre = filter(lambda m : genre in m['genres'], movies_in_year)
    
    # At this point, the list of movies is going to be very small, and possibly empty
    # We cannot send an empty generator to max() function call, it fails horribly
    # So, we convert the generator to a in-memory tuple, and then call most_popular_movie
    movies_in_year_in_genre = tuple(movies_in_year_in_genre)
    if movies_in_year_in_genre:
        return most_popular_movie(movies_in_year_in_genre)
    else:
        return None        
    
def get_all_years(movies):
    movies_with_release_date = filter(lambda m : operator.truth(m['release_date']), movies)
    years_possibly_duplicate = map(lambda m : m['release_date'].tm_year, movies_with_release_date)
    return sorted(list(unique_everseen(years_possibly_duplicate)))
    
def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element

def printPopularMovies():
    file = open("../Popular_Movies/Popular_Movies.txt")
    data = file.read()
    file.close()
    import tkinter as tk
    master = tk.Tk()
    #master.geometry("200x50")
    master.configure(background="#000980")
    scrollbar = tk.Scrollbar(master)
    scrollbar.pack(side="right", fill="y")
    text = tk.Text(master, yscrollcommand=scrollbar.set)
    text.insert("1.0", data)
    text.pack()
    # make text widget readonly
    text.configure(state="disabled", highlightthickness=0)
    scrollbar.config(command=text.yview)
    #root.geometry('%dx%d+%d+%d' % (width,height,x,y))
    master.geometry('%dx%d+%d+%d' % (400,350,500,150))
    master.mainloop()
    '''
    data = file.read()
    file.close()
    root1 = Tk()
    Results = Label(root1, text = data)
    Results.grid(row = 1, column = 1)
    #root.geometry('%dx%d+%d+%d' % (width,height,x,y))
    root1.geometry('%dx%d+%d+%d' % (220,450,500,150))
    '''
                
def main():
    movies = get_movies(open('../data/ml-100k/u.item'), open('../data/ml-100k/u.data'))
    
    movies = movies.values()
    write_file = open('../Popular_Movies/Popular_Movies.txt', 'w')
    write_file.write("----- Most Popular Movie -----\n")
    write_file.write(most_popular_movie(movies)['name']+"\n")
    write_file.write("\n")
    write_file.write("----- Most Watched Movie -----\n")
    write_file.write(most_watched_movie(movies)['name']+"\n")
    write_file.write("\n")
    write_file.write("----- Most Watched Genre -----\n")
    write_file.write(most_watched_genre(movies)+"\n")
    write_file.write("\n")
    
    write_file.write("----- Popular Movie By Genre -----")
    write_file.write("\n")
    
    for genre in all_genres:
        write_file.write("%s : %s" % (genre, most_popular_movie_for_genre(movies, genre)['name']+"\n"))
                         
    write_file.close()
    
    print("Most Popular Movie : %s" % most_popular_movie(movies)['name'])
    print("\n")

    print("Most Watched Movie : %s" % most_watched_movie(movies)['name'])
    print("\n")
    
    print("Most Watched Genre : %s" % most_watched_genre(movies))
    print("\n")
    
    print("\n")
    print("=========================")
    print("Popular Movie By Genre")
    print("=========================")
    for genre in all_genres:
        print("%s : %s" % (genre, most_popular_movie_for_genre(movies, genre)['name']))
    print("===================================================================================================")
    printPopularMovies()
    