import json
import tmdbsimple as tmdb
from dateutil import parser
from datetime import datetime, timedelta
tmdb.API_KEY = '0fee9e05c566948369b71f0cb4e6cef6'
import requests
from tkinter import *

def printFbRecommendation():
    file = open("../Facebook_module/FB_Recommendations1.txt")
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
    master.geometry('%dx%d+%d+%d' % (250,150,900,270))
    master.mainloop()
    '''
    data = file.read()
    file.close()
    root1 = Tk()
    Results = Label(root1, text = data)
    Results.grid(row = 1, column = 1)
    #root.geometry('%dx%d+%d+%d' % (width,height,x,y))
    root1.geometry('%dx%d+%d+%d' % (150,150,900,270))
    '''

def extra():
    print("Inside Extra")
    root = Tk()
    button1 = Button(root, text="Check the Recommendations",fg="white",bg="blue",font = "Verdana 10 bold",command=printFbRecommendation)
    button1.pack()
    #root.geometry('%dx%d+%d+%d' % (width,height,x,y))
    root.geometry('%dx%d+%d+%d' % (300,50,500,320))
    root.mainloop()
      
#calculate the number of lines in the file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


#return date format according to imdb
def resultant_md(movie_date):
    return parser.parse(movie_date).strftime('%Y-%m-%d')

def main_part():
    #call len function to calculate the number of lines and print it
    len=file_len("../Facebook_module/movie-fb.txt")
    #print(len)

    #opening fb movie and date files
    f_movie=open('../Facebook_module/movie-fb.txt','r')
    f_date=open('../Facebook_module/date-fb.txt','r')
    #user_fbmovie_rating=open('fb-rating.txt','w')
    write_file = open('../Facebook_module/FB_Recommendations.txt', 'w')


    #print("RATE THE FOLLOWING MOVIES:")
    print("RECOMMENDATIONS BASED ON FACEBOOK LIKED MOVIES:")
    for var in list(range(len)):
        n=2
        count=0
        #reading first lines from fb movies and date file
        movie_name=f_movie.readline()
        #print(movie_name)
        movie_date_fb=f_date.readline()
        movie_date_fb=movie_date_fb.rstrip('\n')
        default_date="9999"

        #if there exists release date obtained from fb then convert to yyyy-mm-dd format
        if(movie_date_fb!=str(default_date)):
            fbdate_converted=resultant_md(movie_date_fb)
            a,b,c=fbdate_converted.split("-")
            #print("a:"+a+"    b:"+b)

            #search for tmdb-id of the movie
            search = tmdb.Search()
            response = search.movie(query=movie_name)
            for s in search.results:
                ans_movie_id=0000
                imdb_rd=s['release_date']
                #print(imdb_rd)
                if(imdb_rd != ""):
                    x,y,z=imdb_rd.split("-")
                    #print(x)
                    #print(y)
                    if(x==a and y==b):
                        #print("x:"+x+"   a:"+a)
                        #print("y:"+y+"   a:"+b)
                        ans_movie_id=s['id']
                        ans_movie_name=s['title']
                        break
                    
                    # print(movie_date_fb+'yo')
            #print( ans_movie_id)
            #print( ans_movie_name)
            #print("RECOMMENDATIONS :=")
            if(ans_movie_id!=0000):
                movie = tmdb.Movies(ans_movie_id)
                #response=movie.  similar_movies()
                url1 = "https://api.themoviedb.org/3/movie/"
                url2=str(ans_movie_id)+"/recommendations?api_key=0fee9e05c566948369b71f0cb4e6cef6&language=en-US&page=1"
                url=str(url1+url2)
                payload = "{}"
                response = requests.request("GET", url, data=payload)

                #print(response.text)



                #print(response)
                with open('../Facebook_module/similar1.json', 'w') as outfile:
                    json.dump(response.json(), outfile)
            
                json_file = open('../Facebook_module/similar1.json','r')
                j = json.load(json_file)
                json_file.close()
                egg=j['results']
                #print(egg)
                #print("xxxxxx")
                for segg in egg:
                    if count==n:
                        break
                    else:
                        if(segg["original_language"] == 'en'):
                            #print("yyyyyyy")
                            current_movie = segg['original_title']
                            #print(current_movie)
                            write_file.write(current_movie+"\n")
                            count += 1
        
                        #rating=input("rating(1-5):")
                        #user_fbmovie_rating.write(rating+"\n")
            #print("=============================================")
    #else:
        #user_fbmovie_rating.write("-1"+"\n")
#user_fbmovie_rating.close()
    write_file.close()
    extra()
    
    
    #print("==========================================================================")
    f = open("../Facebook_module/FB_Recommendations.txt", "r")
    fp2 =open('../Facebook_module/FB_Recommendations1.txt', 'w')
    lines = set(f.readlines())
    for line in lines:
        fp2.write(line)
    '''
    for line in lines:
        print(line)
    print("==========================================================================")
    '''
#main_part()
