from Hybrid_Module import fetch_recommendations
import pandas as pd
from wsgiref.headers import Headers
#import numpy as np
from tkinter import *

id=0

root = Tk()
def getUserID():
    try:
        global id
        id = int(idEntry.get())
        print("ID: ",id)
    except ValueError:
        print("Value is wrong")
        if id in range(1, 943):
            print("Nice input") 

'''
def show_entry_fields():
    print(" %s \n" % (idEntry.get()))
'''
                      
Label(root, text="Enter User ID: ").grid(row=0)

idEntry = Entry(root)

idEntry.grid(row=0, column=1)

Button(root, text='Submit', command=getUserID).grid(row=1, column=1, sticky=W, pady=4)
#Button(root, text='Show', command=show_entry_fields).grid(row=1, column=2, sticky=W, pady=4)
Button(root, text='Next', command=root.quit).grid(row=1, column=3, sticky=W, pady=4)

#root.geometry('%dx%d+%d+%d' % (width,height,x,y))
root.geometry('%dx%d+%d+%d' % (430,180,450,250))
root.mainloop( )

nt=['i','age','gender','occupation_id']
np=['id','occupation']
df=pd.read_csv("../Hybrid_Module/users.csv",sep="\t",header=None,names=nt)
df2=pd.read_csv("../Hybrid_Module/occupations.csv",sep="\t",header=None,names=np)
#print(df)
print("======================================================")
#id=int(input("Enter user id:"))
#print(df.iloc[[x-1]])
print("ID: ",id)
df1=df.iloc[[id-1]]
age=df1["age"].item()
gender=df1["gender"].item()
occupation_id=df1["occupation_id"].item()
df3=df2.iloc[[occupation_id-1]]
#print(int(age)) 
#print(str(gender))   
occupation=df3["occupation"].item()
#print(str(occupation))

def mainpart():
    # Get list of top n movies
    print("----------",age)
    print("----------",gender)
    print("----------",occupation)
    movies = fetch_recommendations.top_movies(5,fetch_recommendations.sim_users_ratings(age, gender.upper(), occupation.lower())) 
    fp=open("../Hybrid_Module/Hybrid_Recommendations.txt","w")
    for var in list(range(5)):
        print(var)
        fp.write(movies[var]+"\n")
        print(movies[var])
    fp.close()  

#mainpart()
#inp=input("Press r to continue:")
from Hybrid_Module import item_based as rec
#if(inp=="r"):
rec.getId(str(id))