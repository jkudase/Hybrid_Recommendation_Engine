from User_Based_Module import get_recommendations
from tkinter import *

age=0
gender=''
occupation=''
maxCount=0
    
#def getInput():
root = Tk()

def getDetails():
    try:
        global age
        global gender
        global occupation
        global maxCount
        
        age = int(ageEntry.get())
        print("Age: ",age)
        
        gender = genderEntry.get()
        print("Gender: ",gender)
        
        occupation = occupationEntry.get()
        print("Occupation: ",occupation)
        
        maxCount = int(numRecommEntry.get())
        print("Count",maxCount)

    except ValueError:
        print("Value is wrong")
    if age in range(18, 66):
        print("Nice input")
    if gender.upper() in ('M', 'F'):
        print("Nice input")
    
    if occupation.lower() in ('administrator', 'artist', 'doctor', 'educator', 'engineer', 'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer', 'librarian', 'marketing', 'none', 'other', 'programmer', 'retired', 'salesman', 'scientist', 'student', 'technician', 'writer'):
        print("Nice input")
            
    if maxCount in range(1, 10):
        print("Nice input")

'''
def show_entry_fields():
    print("Age: %s\nGender: %s\nOccupation: %s\nNumber of Recommendations: %s\n" % (ageEntry.get(), genderEntry.get(),occupationEntry.get(),numRecommEntry.get()))
'''
           
Label(root, text="Age").grid(row=0)
Label(root, text="Gender").grid(row=1)
Label(root, text="Occupation").grid(row=2)
Label(root, text="No. of Recommendations").grid(row=3)

ageEntry = Entry(root)
genderEntry = Entry(root)
occupationEntry = Entry(root)
numRecommEntry =Entry(root)

ageEntry.grid(row=0, column=1)
genderEntry.grid(row=1, column=1)
occupationEntry.grid(row=2, column=1)
numRecommEntry.grid(row=3, column=1)

Button(root, text='Submit ', command=getDetails).grid(row=4, column=1, sticky=W, pady=4)



#Button(root, text='Show', command=show_entry_fields).grid(row=4, column=2, sticky=W, pady=4)
Button(root, text='Next', command=root.quit).grid(row=4, column=3, sticky=W, pady=4)

#root.geometry('%dx%d+%d+%d' % (width,height,x,y))
root.geometry('%dx%d+%d+%d' % (430,180,450,250))
root.mainloop( )

def printUBRecommendation():
    file = open("../User_Based_Module/UB_Recommendations.txt")
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
    master.geometry('%dx%d+%d+%d' % (300,100,890,350))
    master.mainloop()
    '''
    data = file.read()
    file.close()
    root1 = Tk()
    Results = Label(root1, text = data)
    Results.grid(row = 1, column = 1)
    #root.geometry('%dx%d+%d+%d' % (width,height,x,y))
    root1.geometry('%dx%d+%d+%d' % (300,100,890,350))
    '''
    
def extra():
    print("Inside Extra")
    root2 = Tk()
    button1 = Button(root2, text="Check the Recommendations",fg="white",bg="blue",font = "Verdana 10 bold",command=printUBRecommendation)
    button1.pack()
    #root.geometry('%dx%d+%d+%d' % (width,height,x,y))
    root2.geometry('%dx%d+%d+%d' % (240,50,920,250))
    root2.mainloop()
    
def mainpart():
    # Get list of top n movies
    #getInput()
    print("------------------------------------------------------------------------------------------------------------------")
    print("Age: %s\nGender: %s\nOccupation: %s\nNumber of Recommendations: %s\n" % (age, gender.upper(), occupation.lower(),maxCount))
    
    movies = get_recommendations.top_movies(maxCount,get_recommendations.sim_users_ratings(age, gender.upper(), occupation.lower())) 
    write_file = open('../User_Based_Module/UB_Recommendations.txt', 'w')
    for var in list(range(maxCount)):
        #print(movies[var])
        write_file.write(movies[var]+"\n")
    write_file.close()
    
    extra()

mainpart()