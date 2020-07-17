from tkinter import *
from Main_Start import menu

root=Tk()
   
    
headingLabel = Label(root,text="Movie Recommendation",bg="yellow",fg="black", font = "Helvetica 16 bold italic")
headingLabel.pack(fill=X)

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

popularButton = Button(topFrame,text=" POPULAR MOVIES",fg="white",bg="blue",font = "Verdana 10 bold",command=menu.popular_movies)
fbButton=Button(topFrame,text=" USING FACEBOOK",fg="white",bg="blue",font = "Verdana 10 bold",command=menu.using_fb)
userBasedButton= Button(topFrame,text="USING BASIC DETAILS",fg="white",bg="blue",font = "Verdana 10 bold",command=menu.basic_filters)
itemBasedButton=Button(topFrame,text="BY RATING MOVIES",fg="white",bg="blue",font = "Verdana 10 bold",command=menu.rating_movies) 
hybridButton = Button(topFrame,text="BY INPUTTING USER ID",fg="white",bg="blue",font = "Verdana 10 bold",command=menu.hybrid_rec) 
infoFetcherButton =Button(topFrame,text="LOCAL MOVIE INFORMATION",fg="white",bg="blue",font = "Verdana 10 bold",command=menu.moviefn) 
exitButton =Button(topFrame, text='Quit',fg="white",bg="red",font = "Verdana 10 bold",command=root.quit)

popularButton.pack(fill=X)
fbButton.pack(fill=X)
userBasedButton.pack(fill=X)
itemBasedButton.pack(fill=X)
hybridButton.pack(fill=X)
infoFetcherButton.pack(fill=X)
exitButton.pack(fill=X)


#root.geometry('%dx%d+%d+%d' % (width,height,x,y))
root.geometry('%dx%d+%d+%d' % (300,240,100,250))
root.mainloop()