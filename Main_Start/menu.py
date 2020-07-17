import webbrowser
import subprocess
from Facebook_module import fb_recommend

def menu():
    print("GET RECOMMENDED IN THE FOLLOWING WAYS:-")
    print("-------------------------------------------------------------")
    print("1. USING FACEBOOK")
    print("2. USING BASIC FILTERS")
    print("3. BY RATING MOVIES")
    print("4. HYBRID MODULE")
    print("5.Local Recommender")
    x=input("I'll CHOOSE OPTION :")
    return x;

def go_again():
    z=input("Press c to continue or e to exit:")
    if(z=="c"):
        print("==============================================================================")
        x=menu()
        choosen_option(x)
    elif(z=="e"):
        exit()
    else:
        print("Error: WRONG INPUT")
        go_again()
        
    
def using_fb():
    print("using fb")
    # webbrowser.get('chrome')
    webbrowser.open('http://localhost/BE_Movie_Recommendation/Facebook_module/index.php')
    a=input("INPUT r TO RUN THE ALGO:")
    if(a=="r"):
        fb_recommend.main_part() 
    go_again()


def  basic_filters():
    print(" Loading...")
    from User_Based_Module import start
    start.mainpart()
    go_again()

def rating_movies():
    from Item_Based_Module import rating_based as rs
    rs.processID()
    go_again()
    

def hybrid_rec():
    from Hybrid_Module import user_based as hy
    hy.mainpart()
    go_again()
    
def moviefn():
    from Details_Finder import details_finder as st
    st.main()
    go_again()
    
def popular_movies():
    from Popular_Movies import popular_movies
    popular_movies.main()
    
def choosen_option(x):
    if x == '1':
        using_fb()
    elif x == '2':
        basic_filters()
    elif x=='3':
        rating_movies()
    elif x=='4':
        
        hybrid_rec()
    elif x=='5':
        moviefn()
    else:
        print("ERROR: YOU HAVE ENTERED WRONG CHOICE....PLEASE ENTER AGAIN")
        x=menu();
        choosen_option(x)
        
def main1():
    x=menu()
    choosen_option(x)

