import sys
import os
import omdb
import glob
import operator
import pandas as pd
reserved = ['EXTENDED','REMASTERD','DIRECTORS','UNRATED','AlTERNATE']
from tkinter import *

root = Tk()

dirPath=" "
#F:\test movies
def printLMDetails():
	file = open("../Details_Finder/DF_Details.txt")
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
	master.geometry('%dx%d+%d+%d' % (870,280,300,200))
	master.mainloop()
	
'''	
def printLMDetails():
	file = open("../Local_Recommender/LM_Details.txt")
	data = file.read()
	file.close()
	root1 = Tk()
	Results = Label(root1, text = data)
	Results.grid(row = 1, column = 0)
	#root.geometry('%dx%d+%d+%d' % (width,height,x,y))
	root1.geometry('%dx%d+%d+%d' % (940,160,200,350))
'''
	
def extra():
	print("Inside Extra")
	root2 = Tk()
	button1 = Button(root2, text="Check the Details",fg="white",bg="blue",font = "Verdana 10 bold",command=printLMDetails)
	button1.pack()
	#root.geometry('%dx%d+%d+%d' % (width,height,x,y))
	root2.geometry('%dx%d+%d+%d' % (240,50,920,250))
	root2.mainloop()
	
def getDirectory():
	global dirPath
	dirPath = dirEntry.get()
	print("Path: ",dirPath)

def search(list):
	dic = {}
	plot ={}
	actors={}
	director={}
	genre={}
	err_cnt = 0
	for i in list:
		try:
			obj = omdb.title(i)
			#obj2 = omdb.get(title=i,fullplot=False)
			
			if(obj != []):
				dic[i] = obj.imdb_rating
				#print(dic[i])
				plot[i] =  obj.plot
				#print(plot[i])
				actors[i]=obj.actors
				#print(actors[i])
				director[i]=obj.director
				#print(actors[i])
				genre[i]=obj.genre
				#print(actors[i])
				
		except:
			err_cnt+=1
	return (dic,plot,actors,director,genre)

def clean(raw_list):
	#print(raw_list)
	l = []
	for i in raw_list:
		cl = i
		if('(' in cl):
			cl = i.split('(')
			#print("This is cl after if:",cl)
			cl = cl[0]
		#print("This is bahar wala cl:",cl)
		for j in reserved:
		  	if(j in cl):
		  		cl=cl.split(j)
		  		#print("this is j:",j)
		  		cl = cl[1].strip(" ")
		  		#print("This is cl after .......................for-if:",cl)
		l.append(cl)
	return l

def main():
	global dirPath
	omdb.set_default('tomatoes', True)
	print(dirPath)
	#dirPath = input("Enter directory:")
	#if(len(sys.argv) ==  2):
		#dirPath = sys.argv[1]
	raw_movies = os.listdir(dirPath)
	#print(raw_movies)
	print('Cleaning.....')
	l = clean(raw_movies)
	print('Retreiving Info...')
	info,plot,actors,director,genre = search(l)
	#print(info)
	#print(plot)
	#print(actors)
	#print(director)
	#print(genre)
	
	sorted_x = sorted(info.items(), key=operator.itemgetter(1))
	sorted_x = sorted_x[::-1]
	print(sorted_x)
	f=open("../Details_Finder/DF_Details.txt","w")
	print(sorted_x)
	for i in sorted_x:
		f.write("\n")
		f.write("MOVIE NAME:"+i[0]+"\n")
		f.write("IMDb RATING:"+str(i[1])+"\n")
		f.write("GENRE:"+genre[i[0]]+"\n")
		f.write("ACTORS:"+actors[i[0]]+"\n")
		f.write("DIRECTOR:"+director[i[0]]+"\n")
		f.write("PLOT:"+plot[i[0]]+"\n")
		f.write("\n")
	
	
		print("****************************");
		print("MOVIE NAME:",i[0])
		print("IMDb RATING:",str(i[1]))
		print("GENRE:",genre[i[0]])
		print("ACTORS:",actors[i[0]])
		print("DIRECTOR:",director[i[0]])
		print("PLOT:",plot[i[0]])
	f.close()
	
	extra()
		#print(i[0]+ ' ---------------' + str(i[1])+"---------------"+plot[i[0]]+"---------------------"+actors[i[0]])
	# search = omdb.title('The Matrix')
	# print(search.imdb_rating)
	# print(search.tomato_rating)
'''
def show_entry_fields():
	print(" %s \n" % (dirEntry.get()))
'''
	
Label(root, text="Enter Directory: ").grid(row=0)

dirEntry = Entry(root)

dirEntry.grid(row=0, column=1)

Button(root, text='Submit', command=getDirectory).grid(row=1, column=1, sticky=W, pady=4)
#Button(root, text='Show', command=show_entry_fields).grid(row=1, column=2, sticky=W, pady=4)
Button(root, text='Next', command=root.quit).grid(row=1, column=3, sticky=W, pady=4)

#root.geometry('%dx%d+%d+%d' % (width,height,x,y))
root.geometry('%dx%d+%d+%d' % (430,180,450,250))
root.mainloop( )

main()