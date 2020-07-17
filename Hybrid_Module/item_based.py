import pandas as pd
import webbrowser
import csv
from tkinter import *

maxCount=5

root = Tk()

def printHybridRecommendation():
    file = open("../Hybrid_Module/Hybrid_Recommendations1.txt")
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
    button1 = Button(root2, text="Check the Recommendations",fg="white",bg="blue",font = "Verdana 10 bold",command=printHybridRecommendation)
    button1.pack()
    #root.geometry('%dx%d+%d+%d' % (width,height,x,y))
    root2.geometry('%dx%d+%d+%d' % (240,50,920,250))
    root2.mainloop()
    
def getId(i):
    global maxCount
    count=0
    #print("rating_movies")
    #i=input("ENTER YOUR USER-ID:")
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
    my_ratings = user_ratings.loc[int(i)].dropna() 
    df1=pd.DataFrame(my_ratings)
    
    col1=["name","value"]
    df1.to_csv('../Hybrid_Module/MyRatings.csv',sep='\t',header=False)
    datfr=pd.read_csv("../Hybrid_Module/MyRatings.csv",sep="\t",names=col1,
                      usecols=range(2),encoding='latin-1')
    x2=datfr["name"]
    x2.to_csv("../Hybrid_Module/RatedMovies",index=False)

    sim_candidates = pd.Series()
    #print("*****************************************************************************************")
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
    
    sim_candidates = sim_candidates.groupby(sim_candidates.index).sum()
    
    sim_candidates.sort_values(inplace=True,ascending=False)
    #print("Before recommending:",sim_candidates)
    dataf=pd.DataFrame(sim_candidates)
    
    col=["name","value"]
    dataf.to_csv('../Hybrid_Module/CandidateSimilarity',sep='\t',header=False)
    df2=pd.read_csv("../Hybrid_Module/CandidateSimilarity",sep="\t",names=col,
                      usecols=range(2))
    dfd=df2["name"]
    dfd.to_csv("../Hybrid_Module/UnratedMovies",index=False)
    
    f2=open("../Hybrid_Module/UnratedMovies","r")
    f3=open("../Hybrid_Module/Hybrid_Recommendations.txt","a")
    for line2 in f2:
        m=0
        x=line2.strip("\n")
    

        f1=open("../Hybrid_Module/RatedMovies","r")
        for line1 in f1:
            if(x==line1.strip("\n")):
                m=1
        f1.close()
        if(m==0 and count!=maxCount):
                    f3.write(x)
                    f3.write("\n")
                    count+=1
    f3.close()
    print("==========The recommendations are as follows:==========")
    
    f=open("../Hybrid_Module/Hybrid_Recommendations.txt","r")
    fp1=open("../Hybrid_Module/Hybrid_Recommendations1.txt","w")
    lines = set(f.readlines())
    for line in lines:
        fp1.write(line)
    fp1.close()
    '''
    max=0
    for line in fp1:
        if(max !=10):
            print(line)
            max=max+1
        else:
            break
    '''
    f.close()
    extra()
#getId(2)