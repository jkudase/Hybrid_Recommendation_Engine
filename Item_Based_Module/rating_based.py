import pandas as pd
import webbrowser
import csv
from tkinter import *

id=" "
m1=" "
m2=" "
r1=" "
r2=" "
maxCount=0

root = Tk()

def printIBRecommendation():
    file = open("../Item_Based_Module/IB_Recommendations.txt")
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
    master.geometry('%dx%d+%d+%d' % (380,160,920,350))
    master.mainloop()
    
    '''
    data = file.read()
    file.close()
    root1 = Tk()
    Results = Label(root1, text = data)
    Results.grid(row = 1, column = 1)
    #root.geometry('%dx%d+%d+%d' % (width,height,x,y))
    root1.geometry('%dx%d+%d+%d' % (240,160,920,350))
    '''
    
def extra():
    print("Inside Extra")
    root2 = Tk()
    button1 = Button(root2, text="Check the Recommendations",fg="white",bg="blue",font = "Verdana 10 bold",command=printIBRecommendation)
    button1.pack()
    #root.geometry('%dx%d+%d+%d' % (width,height,x,y))
    root2.geometry('%dx%d+%d+%d' % (240,50,920,250))
    root2.mainloop()
    
def getRatings():
    try:
        global id
        global m1
        global m2
        global r1
        global r2
        global maxCount
        id = int(idEntry.get())
        print("ID: ",id)
        m1 = int(movie1Entry.get())
        print("Movie 1:",m1)
        m2 = int(movie2Entry.get())
        print("Movie 2:",m2)
        r1 = int(rating1Entry.get())
        print("Rating 1:",r1)
        r2 = int(rating2Entry.get())
        print("Rating 2:",r2)
        maxCount = int(numRecommEntry.get())
        print("Count",maxCount)
        #label.configure(text=age)
    except ValueError:
        print("Value is wrong")
    if id in range(1, 943):
        print("Nice input") 
    if m1 in range(1, 1682):
        print("Nice input")
    if m2 in range(1, 1682):
        print("Nice input")
    if r1 in range(1,5):
        print("Nice input")
    if r2 in range(1,5):
        print("Nice input")
    if maxCount in range(1, 10):
        print("Nice input")
        
def processID():
    global maxCount
    count=0
    #print("rating_movies")
    #i=input("ENTER YOUR USER-ID:")##################################
    #webbrowser.open('http:\\localhost\BE_Movie_Recommendation\Item_Based_Module\php_html_table_data_filter.php')
    #m1=input("INPUT THE MOVIE INDEX:")###################################
    #r1=input("INPUT THE RATING(1-5):")#####################################
    global id
    global m1
    global r1
    global m2
    global r2
    id=str(id)
    m1=str(m1)
    r1=str(r1)
    m2=str(m2)
    r2=str(r2)
    #print(type(id))
    x=id+" "+m1+" " +r1+" "+"xxxxxx"
    with open('../data/ml-100k/u1.base', 'a') as f:
        f.writelines("\n")
        f.writelines(id)
        f.writelines("\t")
        f.writelines(m1)
        f.writelines("\t")
        f.writelines(r1)
        f.writelines("\t")
        f.writelines("xxxxxx")
        f.close()
    #m2=input("INPUT THE MOVIE INDEX:")##################################
    #r2=input("INPUT THE RATING(1-5):")#################################
    x=id+" "+m2+" " +r2+" "+"xxxxxx"
    with open('../data/ml-100k/u1.base', 'a') as f:
        f.writelines("\n")
        f.writelines(id)
        f.writelines("\t")
        f.writelines(m2)
        f.writelines("\t")
        f.writelines(r2)
        f.writelines("\t")
        f.writelines("xxxxxx")
        f.close()
        
    r_cols = ["user_id", "movie_id", "rating"]
    ratings = pd.read_csv("../data/ml-100k/u1.base", sep="\t", names=r_cols,
                      usecols=range(3))
    m_cols = ["movie_id", "title"]
    movies = pd.read_csv("../data/ml-100k/u.item", sep="|", names=m_cols, 
                     usecols=range(2), encoding='latin-1')
    ratings = pd.merge(ratings, movies)
    user_ratings = ratings.pivot_table(index=["user_id"], columns=["title"], values="rating")
    
    corr_matrix = user_ratings.corr(method="pearson", min_periods=100)
    '''
    df=pd.DataFrame(corr_matrix)
    print(df)
    '''
    #print("Correlation matrix:",corr_matrix)
    df=pd.DataFrame(corr_matrix)
    #print(df)
    #df.to_csv('movdf.csv', sep='\t')
    #print(type(corr_matrix))
    my_ratings = user_ratings.loc[int(id)].dropna() 
    #print("*****************************************************************************************")
    #print("THE USER HAS MADE THE FOLLOWING RATINGS:\n", my_ratings)
    
    #print("*****************************************************************************************")
    df1=pd.DataFrame(my_ratings)
    
    col1=["name","value"]
    df1.to_csv('MyRatings.csv',sep='\t',header=False)
    datfr=pd.read_csv("MyRatings.csv",sep="\t",names=col1,
                      usecols=range(2),encoding='latin-1')
    x2=datfr["name"]
    x2.to_csv("RatedMovies.csv",index=False)
    
    sim_candidates = pd.Series()
    print("*****************************************************************************************")
    #print("len(my_ratings)::::::",len(my_ratings))
    for i in range(0, len(my_ratings.index)):
        #print("my_ratings.index[i]:",my_ratings.index[i])
        sims = corr_matrix[my_ratings.index[i]].dropna()
        df1=pd.DataFrame(sims)
        #print("SIMS:\n",df1)
        sims = sims.map(lambda x: x * my_ratings[i])  # We give weight values ​​given depending on the user's grading
        sim_candidates = sim_candidates.append(sims)
    df=pd.DataFrame(sim_candidates)
    #print(df)
    sim_candidates.sort_values(inplace=True, ascending=False)
    
    '''
    print("*****************************************************************************************")
    print(sim_candidates)
    print("*****************************************************************************************")
    '''
    
    sim_candidates = sim_candidates.groupby(sim_candidates.index).sum()
    
    '''
    print("*****************************************************************************************")
    print("sim_candidates index:",sim_candidates.index)
    print("*****************************************************************************************")
    '''
    
    sim_candidates.sort_values(inplace=True,ascending=False)
    #print("Before recommending:",sim_candidates)
    dataf=pd.DataFrame(sim_candidates)
    
    col=["name","value"]
    dataf.to_csv('MovieSimilarity.csv',sep='\t',header=False)
    df2=pd.read_csv("MovieSimilarity.csv",sep="\t",names=col,
                      usecols=range(2))
    dfd=df2["name"]
    dfd.to_csv("UnratedMovies.csv",index=False)
    
    f2=open("UnratedMovies.csv","r")
    f3=open("../Item_Based_Module/IB_Recommendations.txt", "w")
    
    for line2 in f2:
        m=0
        x=line2.strip("\n")
    
        f1=open("RatedMovies.csv","r")
        for line1 in f1:
            if(x==line1.strip("\n")):
                m=1
        f1.close()
        if(m==0 and count!=maxCount):
            #print("max count value",maxCount)
            f3.write(x)
            f3.write("\n")
            count+=1
    f3.close()
    print("==========The recommendations are as follows:==========")
    
    extra()

'''    
def show_entry_fields():
    print(" %s %s %s %s %s %s\n" % (idEntry.get(), movie1Entry.get(),movie2Entry.get(),rating1Entry.get(),rating2Entry.get(),numRecommEntry.get()))
'''
    
webbrowser.open('http:\\localhost\BE_Movie_Recommendation\Item_Based_Module\movie_DB.php')
Label(root, text="User ID").grid(row=0)
Label(root, text="Movie 1").grid(row=1)
Label(root, text="Movie 2").grid(row=2)
Label(root, text="Rating 1").grid(row=1 , column=2)
Label(root, text="Rating 2").grid(row=2, column=2)
Label(root, text="No. of Recommendations").grid(row=3)

idEntry = Entry(root)
movie1Entry = Entry(root)
movie2Entry = Entry(root)
rating1Entry = Entry(root)
rating2Entry = Entry(root)
numRecommEntry =Entry(root)

idEntry.grid(row=0, column=1)
movie1Entry.grid(row=1, column=1)
movie2Entry.grid(row=2, column=1)
rating1Entry.grid(row=1,column=3)
rating2Entry.grid(row=2,column=3)
numRecommEntry.grid(row=3, column=1)

Button(root, text='Submit', command=getRatings).grid(row=4, column=1, sticky=W, pady=4)
#Button(root, text='Show', command=show_entry_fields).grid(row=4, column=2, sticky=W, pady=4)
Button(root, text='Next', command=root.quit).grid(row=4, column=3, sticky=W, pady=4)

#root.geometry('%dx%d+%d+%d' % (width,height,x,y))
root.geometry('%dx%d+%d+%d' % (430,180,450,250))
root.mainloop( )


#processID()