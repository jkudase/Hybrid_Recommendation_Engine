import os
import math 
import numpy as np
import pandas as pd

def load_data(file_name, npy, path = os.path.dirname(os.getcwd()) + '/data/ml-100k/'):
    "Loads data into matrix, filling in empty ratings with 3"
    
    # Read in file
    rnames = ['user', 'movie', 'rating', 'timestamp']
    df = pd.read_table(path + file_name, sep = '\t', header = None, names = rnames,encoding='latin-1')
    
    
    '''
    print("ddddddddddddffffffffffffffff:")
    print(df)
    '''
    
    
    # Determine the number of unique users and movies
    num_users = len(np.unique(df[['user']].values))
    num_movies = len(np.unique(df[['movie']].values))
    '''
    print("num_users:")
    print(num_users)
    print("\n")
    print("num_movies:")
    print(num_movies)
    '''

    # Matrix of size num_users x num_movies (rows x cols)
    matrix = [[3 for _ in range(num_movies)] for _ in range(num_users)]
    
   
    
    
    '''
    print("===========================================================================")
    print(df['user'][1]-1 )
    print(df['movie'][1]-1 )
    print(df['rating'][1])
    '''
    
    
    # Fill in matrix from data
    for index in df.index: 
        user = df['user'][index] 
        movie = df['movie'][index] 
        rating = df['rating'][index] 
        matrix[user - 1][movie - 1] = rating

    # Check for which version of kmeans to use
    if npy == 1:
        m = np.array(matrix)
        m.astype(float)
    else:
        m = matrix
    
    #print('Data loaded:')
    return m
    

def testing_load_data(file_name, npy, path = os.path.dirname(os.getcwd()) + '/data/ml-100k/'):
    "Loads data into matrix, filling in empty ratings with 0"

    # Read in file
    rnames = ['user', 'movie', 'rating', 'timestamp']
    df = pd.read_table(path + file_name, sep = '\t', header = None, names = rnames,encoding='latin-1')

    # Matrix of size num_users x num_movies (rows x cols)
    matrix = [[0 for _ in range(1682)] for _ in range(943)]

    # Fill in matrix from data
    for index in df.index: 
        user = df['user'][index] 
        movie = df['movie'][index] 
        rating = df['rating'][index] 
        matrix[user-1][movie-1] = rating

    # Convert to numpy array
    m = np.array(matrix)
    m.astype(float)

    return m


def user_load_data(file_name, path = os.path.dirname(os.getcwd()) + '/data/ml-100k/'):
    "Loads in user data"

    # Read in file 
    rnames = ['age', 'gender', 'occupation', 'zipcode']
    df = pd.read_csv(path + file_name, delimiter = '|', header=None, names = rnames,encoding='latin-1')
    
    # Convert to list
    dflist = df.values.tolist()
    
    return dflist


def movie_load_data(file_name, path = os.path.dirname(os.getcwd()) + '/data/ml-100k/'):
    "Loads in movie data"

    # Read in file
    df = pd.read_csv(path + file_name, delimiter = '|', header = None,encoding='latin-1')

    # Convert to list
    dflist = df.values.tolist()

    return dflist
