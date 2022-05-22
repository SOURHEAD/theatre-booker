from tkinter import *
from tkinter import messagebox
seather=0
polpo=0
username=password=0
foodlist=[]
l=[]
foodstring=""
pass_word="jiit"    #here is the passwordfor mysql server

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=pass_word,
  database="ooer"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
  l.append(x)
me=False
for i in range(len(l)):
    if "profile" in l[i][0]:
        me=True
if me:
  pass
else:
  mycursor.execute("create table profile (username varchar(255) PRIMARY KEY, password varchar(255) NOT NULL)")

#this is to define the contents of the program
def createtables(): #tables for every movie
    for ooh in povies: #povies:list of movies
        m=True
        for i in h: #h:list of tables in ooer
            for y in i:
                if(ooh==y):  
                    m=False
        if m:
            mycursor.execute("create table %s (username varchar(255) NOT NULL, seat varchar(255) primary key)" %ooh) 
            mydb.commit()


povies=['blackpanther','antman','ironman','doctorstrange','avengersendgame','gotg']
mycursor.execute("show tables")

h=[]
for x in mycursor:
  h.append(list(x))
createtables()




def clear():                               #this is to destroy all .pack() widgets.
    list = x.pack_slaves()
    for l in list:
        l.destroy()
def clear2():                               #this is to destroy all .grid() widgets.
    list = x.grid_slaves()
    for l in list:
        l.destroy()


#This is to clear everything in a tkinter window
        

def intr():                                 #first function for title screen
    x=Tk()
    photo = PhotoImage(file = "cs.png")
    x.title("Welcome to Grande Cinema!")
    x.geometry('1280x720')

    a=Label(x, image = photo)
    a.grid(row=0)
    a.after(3000 , a.master.destroy)
    x.mainloop()

intr()

#this is the first function for introductary screen

def new_ac():                               #this is to use when creating a new account.
    global kkk
    global ull
    kkk=username.get()
    ull=password.get()
    EVANG=False
    for i in kkk:
        if i.isalpha():
            EVANG=True
    if kkk.isalnum() and EVANG:
        enter_into_table()
    else:
        messagebox.showerror(title='Error',message='Please enter alphabets and numbers only,alphabets compulsory,also please read terms and conditions by asking the devs')
        signup()
def cl():                               #this function is for submitting the button
    global kkk
    global ull
    global trodo
    kkk=username.get()
    ull=password.get()

    mycursor.execute("SELECT * FROM profile")
    myresult = mycursor.fetchall()
    for i in myresult:
        if (kkk,ull)==i:
            cancel_or_book()
            break
    else:
        messagebox.showerror(title='Error',message='Invalid Username/Password. Try again')
def enter_into_table():                     #this function is to create an account. 
    try:
        sql = "INSERT INTO profile (username,password) VALUES (%s, %s)"
        val = (kkk,ull )
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo(message='Account Created!')
        login()
    except:
        messagebox.showerror(title='Error',message='Username not available')
        
        
def signup():                               #this is to sign up
    clear2()
    x.configure(bg="dark slate blue")
    x.geometry("1000x570")

    t1=Label(text="SIGN UP",font=("Arial",40,'bold'),bg="dark slate blue",fg='azure') #header
    t1.grid(row=0,column=0,columnspan='2',padx='400',pady='50',sticky='N')

    u_label=Label(x,text="Enter Username:",font=('Calibri',20),bg="dark slate blue",fg='azure')
    u_label.grid(row=1,column=0,sticky='E',pady=15)
    global username
    global password
    username=Entry(x,text="Plese enter username here",font=('Calibri',16))
    username.grid(row=1,column=1,sticky='W',pady=15)

    p_label=Label(x,text="Enter Password:",font=('Calibri',20),bg='dark slate blue',fg='azure')
    p_label.grid(row=2,column=0,sticky='E',pady=15)

    password=Entry(x,text="Enter Password",font=('Calibri',16))
    password.config(show="*") 
    password.grid(row=2,column=1,sticky='W',ipadx='1',ipady='1',pady=15)

    submit_btn=Button(text="Submit",command=new_ac,font=('Arial',15),bg='plum1',relief='raised')
    submit_btn.grid(row=3,column=0,padx=20,pady=60,sticky='E')

    but2=Button(text="Back to login",command=login,font=('Arial',15),bg='plum1',relief='raised')
    but2.grid(row=3,column=1,padx=20,pady=60,sticky='W')
    x.mainloop()
def login():                               #this is to login
    clear2()
    x.configure(bg="dark slate blue")
    x.geometry("1000x570")

    t2=Label(text="LOGIN",font=("Arial",40,'bold'),bg="dark slate blue",fg='azure') #header
    t2.grid(row=0,column=0,columnspan=2,padx=400,pady=50,sticky='N')

    u_label=Label(x,text="Enter Username:",font=('Calibri',20),bg='dark slate blue',fg='azure')
    u_label.grid(row=1,column=0,sticky='E',pady=15)
    global username
    global password

    username=Entry(x,text="username ",font=('Calibri',20))
    username.grid(row=1,column=1,sticky='W',pady=15)

    p_label=Label(x,text="Enter password:",font=('Calibri',20),bg='dark slate blue',fg='azure')
    p_label.grid(row=2,column=0,sticky='E',pady=15)

    password=Entry(x,text="password",font=('Calibri',20))
    password.config(show="*") 
    password.grid(row=2,column=1,sticky='W',pady=15)

    proceed_btn=Button(text="Proceed",command=cl,font=('Arial',15),bg='plum1',relief='raised')
    proceed_btn.grid(row=3,column=0,padx=20,pady=60,sticky='E')

    but2=Button(text="Don't have an account? Sign up!",command=signup,font=('Arial',15),bg='plum1',relief='raised')
    but2.grid(row=3,column=1,padx=20,pady=60,sticky='W')
    x.mainloop()



def cancel_or_book():
    clear2()
    x.configure(bg='dark slate blue')
    x.geometry('450x400')
    b_button=Button(text='BUY TICKETS',command=after_login,font=('Calibri',25,'bold'),bg='plum1',relief='raised')
    b_button.grid(row=0,column=0,padx=100,pady=90,sticky='S')
    c_button=Button(text='CANCELLATION',command=canceltickets,font=('Calibri',25,'bold'),bg='plum1',relief='raised')
    c_button.grid(row=1,column=0,padx=100)     
    
def canceltickets():
    clear2()
    x.configure(bg='dark slate blue')
    print("do we really need to end right now?")
    x.configure(bg="gray10")
    x.geometry("1000x650")

    header=Label(x,text='Select a movie',font=('Calibri',40,'bold'),bg='gray10',fg='SlateGray3')
    header.grid(row=0,column=0,columnspan=3,padx='300',pady='20',sticky='N')

    Antman=PhotoImage(file='antman.png')
    IronMan=PhotoImage(file='ironman.png')
    DoctorStrange=PhotoImage(file='doctorstrange.png')
    AvengersEndgame=PhotoImage(file='avengersendgame.png')
    BlackPanther=PhotoImage(file='blackpanther.png')
    Gotg=PhotoImage(file='gotg.png')
    
    b1=Button(x, text='Black Panther',image=BlackPanther,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: cancel_movie('blackpanther'),bg='gold')
    b2=Button(x, text='Antman',image=Antman,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: cancel_movie('antman'),bg='gold')
    b3=Button(x, text='IronMan',image=IronMan,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: cancel_movie('ironman'),bg='gold')
    b4=Button(x, text='Doctor Strange',image=DoctorStrange,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: cancel_movie('doctorstrange'),bg='gold')
    b5=Button(x, text='Avengers\nEndgame',image=AvengersEndgame,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: cancel_movie('avengersendgame'),bg='gold')
    b6=Button(x, text='Guardians Of\nThe Galaxy',image=Gotg,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: cancel_movie('gotg'),bg='gold')

    b1.grid(row=1,column=0,padx=5,pady=15)
    b2.grid(row=1,column=1,padx=5,pady=15)
    b3.grid(row=1,column=2,padx=5,pady=15)
    b4.grid(row=2,column=0,padx=5,pady=15)
    b5.grid(row=2,column=1,padx=5,pady=15)
    b6.grid(row=2,column=2,padx=5,pady=15)
    x.mainloop()
    
def cancel_movie(mov):
    clear2()
    x.configure(bg="light green")
    print(mov)
    x.geometry('636x610')
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=pass_word,
    database="ooer"
    )
    mycursor = mydb.cursor()
    
    
    scr=Label(x,text='SCREEN HERE',fg='black',bg='lavender',font=('Arial',30,'bold')).grid(row=0,column=1,columnspan=5,ipadx=110,padx=50,pady=80)
    A1=Button(text="A1",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('A1',mov))
    A2=Button(text="A2",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('A2',mov))
    A3=Button(text="A3",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('A3',mov))
    A4=Button(text="A4",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('A4',mov))
    A5=Button(text="A5",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('A5',mov))
    B1=Button(text="B1",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('B1',mov))
    B2=Button(text="B2",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('B2',mov))
    B3=Button(text="B3",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('B3',mov))
    B4=Button(text="B4",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('B4',mov))
    B5=Button(text="B5",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('B5',mov))
    C1=Button(text="C1",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('C1',mov))
    C2=Button(text="C2",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('C2',mov))
    C3=Button(text="C3",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('C3',mov))
    C4=Button(text="C4",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('C4',mov))
    C5=Button(text="C5",bg="lightgreen",font=('Arial',15),relief='raised',command=lambda: pencil('C5',mov))
    backer=Button(text="Back",bg="lightgreen",command=canceltickets,font=('Arial',15))
    jj={"A1":A1,"A2":A2,"A3":A3,"A4":A4,"A5":A5,"B1":B1,"B2":B2,"B3":B3,"B4":B4,"B5":B5,"C1":C1,"C2":C2,"C3":C3,"C4":C4,"C5":C5}
    p=[]
    polpo='select * from '+mov+' where username="'+kkk+'"'
    mycursor.execute(polpo)
    k=mycursor.fetchall()
    for i in k:
        p.append(i[1])
    mycursor.execute("select * from "+mov)
    k=mycursor.fetchall()
    for i in jj:
        if i not in p:
             opi=jj.get(i)
             opi.configure(state='disabled')

    A1.grid(row=1,column=1,ipadx=15,ipady=15,pady=10)
    A2.grid(row=1,column=2,ipadx=15,ipady=15,pady=10)
    A3.grid(row=1,column=3,ipadx=15,ipady=15,pady=10)
    A4.grid(row=1,column=4,ipadx=15,ipady=15,pady=10)
    A5.grid(row=1,column=5,ipadx=15,ipady=15,pady=10)
    B1.grid(row=2,column=1,ipadx=15,ipady=15,pady=10)
    B2.grid(row=2,column=2,ipadx=15,ipady=15,pady=10)
    B3.grid(row=2,column=3,ipadx=15,ipady=15,pady=10)
    B4.grid(row=2,column=4,ipadx=15,ipady=15,pady=10)
    B5.grid(row=2,column=5,ipadx=15,ipady=15,pady=10)
    C1.grid(row=3,column=1,ipadx=15,ipady=15,pady=10)
    C2.grid(row=3,column=2,ipadx=15,ipady=15,pady=10)
    C3.grid(row=3,column=3,ipadx=15,ipady=15,pady=10)
    C4.grid(row=3,column=4,ipadx=15,ipady=15,pady=10)
    C5.grid(row=3,column=5,ipadx=15,ipady=15,pady=10)
    backer.grid(row=4,column=1,columnspan=5,pady=45)
    
def pencil(cancel,mov):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd=pass_word,
      database="ooer"
    )

    mycursor = mydb.cursor()
    clear2()
    x.configure(bg="dark slate blue")
    x.geometry('450x400')
    g='delete from '+mov+' where username="'+kkk+'" and seat="'+cancel+'"'
    mycursor.execute(g)
    print(mov+" seat canceled "+cancel)
    mydb.commit()
    cancel_more=Button(text="Cancel another seat",command=lambda: cancel_movie(mov),bg="plum1",font=('Arial',15))
    backert=Button(text="Cancel food",command=lambda: cancelfood(mov),bg="plum1",font=('Arial',15))
    backer=Button(text="Exit Application",command=x.destroy,bg="plum1",font=('Arial',15))
    disclaimer=Label(x, text='Food from this movie\'s bookings will be cancelled',bg='dark slate blue',font=('Arial',8))
    cancel_more.grid(row=0,column=0,padx=110,pady=40,sticky='S')
    backert.grid(row=1,column=0,padx=110)
    disclaimer.grid(row=2,column=0,padx=110)
    backer.grid(row=3,column=0,padx=110,pady=40)

def cancelfood(mov):
    g='delete from food.'+kkk+' where movie="'+mov+'"'
    mydb.cursor().execute(g)
    mydb.commit()
    messagebox.showerror(title='Done',message='Food has been cancelled.')
    

def after_login(a=''):                               #this is to select movie

    if a=='f':
        clear()
        a=''
    else:
        clear2()
    x.configure(bg="gray10")
    x.geometry("1000x650")

    header=Label(x,text='Select a movie',font=('Calibri',40,'bold'),bg='gray10',fg='SlateGray3')
    header.grid(row=0,column=0,columnspan=3,padx='300',pady='10',sticky='N')
    global Antman
    global IronMan
    global DoctorStrange
    global AvengersEndgame
    global BlackPanther
    global Gotg
    Antman=PhotoImage(file='antman.png')
    IronMan=PhotoImage(file='ironman.png')
    DoctorStrange=PhotoImage(file='doctorstrange.png')
    AvengersEndgame=PhotoImage(file='avengersendgame.png')
    BlackPanther=PhotoImage(file='blackpanther.png')
    Gotg=PhotoImage(file='gotg.png')
    global seather
    seather=0
    b1=Button(x, text='Black Panther \n IMDB 7.3/10',image=BlackPanther,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('blackpanther'),bg='gold')
    b2=Button(x, text='Antman \n IMDB 7.3/10',image=Antman,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('antman'),bg='gold')
    b3=Button(x, text='IronMan \n IMDB 7.9/10',image=IronMan,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('ironman'),bg='gold')
    b4=Button(x, text='Doctor Strange \n IMDB 7.5/10',image=DoctorStrange,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('doctorstrange'),bg='gold')
    b5=Button(x, text='Avengers\nEndgame \n IMDB 8.4/10',image=AvengersEndgame,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('avengersendgame'),bg='gold')
    b6=Button(x, text='Guardians Of\nThe Galaxy \n IMDB 8/10',image=Gotg,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('gotg'),bg='gold')
    global totalseats
    totalseats=[]
    b1.grid(row=1,column=0,padx=5,pady=15)
    b2.grid(row=1,column=1,padx=5,pady=15)
    b3.grid(row=1,column=2,padx=5,pady=15)
    b4.grid(row=2,column=0,padx=5,pady=15)
    b5.grid(row=2,column=1,padx=5,pady=15)
    b6.grid(row=2,column=2,padx=5,pady=15)
    x.mainloop()

def select_movie(name):                               #this is to select and check availibility of seats.
    clear2()
    disableseats()

    x.configure(bg='dark slate blue')
    x.geometry('250x500')
    global moviename
    global yoyo
    moviename=""
    setl=Label(text="Please enter number of seats:",bg='dark slate blue')
    yoyo=Entry(x,text="here")
    set2l=Label(text="",bg='dark slate blue')
    for i in name:
        if i.isalpha():
            moviename+=i
    loc=moviename+".png"
    img=PhotoImage(file=loc)
    hawrah=moviename.lower()
    gnome=gg(hawrah)
    global p
    global seatsleft
    p=[]
    for i in gnome:
        for j in i:
           p.append(j)
    seatsleft=15-len(p)
    center=Label(x,text=name,image=img,compound='top',font=('Calibri',15),fg='black',bg='gold')
    center.image=img
    center.grid(row=1,column=0,padx='55',pady='40')
    setl.grid(row=2,column=0)
    set2l.grid(row=3,column=0)
    yoyo.grid(row=4,column=0)
    set2l.grid(row=5,column=0)
    Button(x,text='Back',font=('Arial'),command=after_login,bg='plum1').grid(row=7,column=0,pady=10)
    Button(x,text='Select Seats',font=('Arial'),command=stiens,bg='plum1').grid(row=6,column=0)


def stiens():                               #this is to show error if a wierd number(0 or <0 or something other than int) is selected for seats.
    global jojo
    jojo=yoyo.get()
    try:
        if int(jojo)<=0:
            messagebox.showerror(title='Error',message='Please refrain from trying to break the program')
            after_login()
        else:
            if(seatsleft<int(jojo)):
                messagebox.showerror(title='Error',message='Not enough seats available')
            else:
                moviesseatelection()
    except ValueError:
        messagebox.showerror(title='Error',message='You ok?')

def gg(la):                                 #this was to create a switch case statement in python using dictionaries so as to not use multiple if else .
    switcher={
                    'blackpanther':blackpanther,
                    'antman':antman,
                   'ironman':ironman,
                    'doctorstrange':doctorstrange,
                   'avengersendgame':avengersendgame,
                   'gotg':gotg
                 }
    return(switcher.get(la))

def disableseats():                         #this is to check which seats have been selected and to disable those which haven't been selected.
    s=('A1','A2','A3','A4','A5','B1','B2','B3','B4','B5','C1','C2','C3','C4','C5')
    povies=['blackpanther',
     'antman',
     'ironman',
     'doctorstrange',
     'avengersendgame',
     'gotg']

    global blackpanther
    global antman
    global ironman
    global doctorstrange
    global avengersendgame
    global gotg

    blackpanther=[]
    antman=[]
    ironman=[]
    doctorstrange=[]
    avengersendgame=[]
    gotg=[]

    for i in povies:
        b=i
        mycursor.execute("select seat from "+i)
        myresult=mycursor.fetchall()
        for x in myresult:
            if x not in gg(i):
                 (gg(i)).append(x)
                 
def seats():#enter values into seat column of tables
    s=('A1','A2','A3','A4','A5','B1','B2','B3','B4','B5','C1','C2','C3','C4','C5')
    for i in povies:
        mycursor.execute("select * from "+i)
        myresult=mycursor.fetchall()
        if myresult==[]:
            for j in s:
                mycursor.execute("INSERT INTO "+i+" (seat) values ('%s')" % j)
                mydb.commit()
        else:
            continue


def moviesseatelection():                  #this function is to select a seat for the user
     global A1,A2,A3,A4,B5,B1,B2,B3,B4,B5,C1,C2,C3,C4,C5
     clear2()
     x.geometry('636x610')
     x.configure(bg='dark slate blue')
     scr=Label(x,text='SCREEN HERE',fg='black',bg='lavender',font=('Arial',30,'bold')).grid(row=0,column=1,columnspan=5,ipadx=110,padx=50,pady=80)
     A1=Button(text="A1",command=lambda: seatpicked('A1',A1),bg="lightgreen",font=('Arial',15),relief='raised')
     A2=Button(text="A2",command=lambda: seatpicked('A2',A2),bg="lightgreen",font=('Arial',15),relief='raised')
     A3=Button(text="A3",command=lambda: seatpicked('A3',A3),bg="lightgreen",font=('Arial',15),relief='raised')
     A4=Button(text="A4",command=lambda: seatpicked('A4',A4),bg="lightgreen",font=('Arial',15),relief='raised')
     A5=Button(text="A5",command=lambda: seatpicked('A5',A5),bg="lightgreen",font=('Arial',15),relief='raised')
     B1=Button(text="B1",command=lambda: seatpicked('B1',B1),bg="lightgreen",font=('Arial',15),relief='raised')
     B2=Button(text="B2",command=lambda: seatpicked('B2',B2),bg="lightgreen",font=('Arial',15),relief='raised')
     B3=Button(text="B3",command=lambda: seatpicked('B3',B3),bg="lightgreen",font=('Arial',15),relief='raised')
     B4=Button(text="B4",command=lambda: seatpicked('B4',B4),bg="lightgreen",font=('Arial',15),relief='raised')
     B5=Button(text="B5",command=lambda: seatpicked('B5',B5),bg="lightgreen",font=('Arial',15),relief='raised')
     C1=Button(text="C1",command=lambda: seatpicked('C1',C1),bg="lightgreen",font=('Arial',15),relief='raised')
     C2=Button(text="C2",command=lambda: seatpicked('C2',C2),bg="lightgreen",font=('Arial',15),relief='raised')
     C3=Button(text="C3",command=lambda: seatpicked('C3',C3),bg="lightgreen",font=('Arial',15),relief='raised')
     C4=Button(text="C4",command=lambda: seatpicked('C4',C4),bg="lightgreen",font=('Arial',15),relief='raised')
     C5=Button(text="C5",command=lambda: seatpicked('C5',C5),bg="lightgreen",font=('Arial',15),relief='raised')
     backer=Button(text="Back",command=after_login,bg="azure",font=('Arial',15))
     jj={"A1":A1,"A2":A2,"A3":A3,"A4":A4,"A5":A5,"B1":B1,"B2":B2,"B3":B3,"B4":B4,"B5":B5,"C1":C1,"C2":C2,"C3":C3,"C4":C4,"C5":C5}
     for i in p:
         opi=jj.get(i)
         opi.configure(state='disabled')

     A1.grid(row=1,column=1,ipadx=15,ipady=15,pady=10)
     A2.grid(row=1,column=2,ipadx=15,ipady=15,pady=10)
     A3.grid(row=1,column=3,ipadx=15,ipady=15,pady=10)
     A4.grid(row=1,column=4,ipadx=15,ipady=15,pady=10)
     A5.grid(row=1,column=5,ipadx=15,ipady=15,pady=10)
     B1.grid(row=2,column=1,ipadx=15,ipady=15,pady=10)
     B2.grid(row=2,column=2,ipadx=15,ipady=15,pady=10)
     B3.grid(row=2,column=3,ipadx=15,ipady=15,pady=10)
     B4.grid(row=2,column=4,ipadx=15,ipady=15,pady=10)
     B5.grid(row=2,column=5,ipadx=15,ipady=15,pady=10)
     C1.grid(row=3,column=1,ipadx=15,ipady=15,pady=10)
     C2.grid(row=3,column=2,ipadx=15,ipady=15,pady=10)
     C3.grid(row=3,column=3,ipadx=15,ipady=15,pady=10)
     C4.grid(row=3,column=4,ipadx=15,ipady=15,pady=10)
     C5.grid(row=3,column=5,ipadx=15,ipady=15,pady=10)
     backer.grid(row=4,column=1,columnspan=5,pady=45)
     x.mainloop() 
     
def whyidk():                               #this function is to create database ooer if not already created
    l=[]
    mycursor.execute("use food")
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        l.append(x)
    me=False
    for i in range(len(l)):
        if kkk in l[i][0]:
            me=True
    if me:
       pass
    else:
       mycursor.execute("create table "+kkk+" (movie varchar(255) , food varchar(255) , type varchar(255) , quantity integer(255))")
    mycursor.execute("use ooer")
  
def totalse():                              #this function is to check total seat number from mysql
    global pp
    pp=[]
    mycursor.execute("use ooer")
    mycursor.execute("select seat from "+moviename+" where username='%s'"%kkk)
    for i in mycursor:
        pp.append(i)
    return pp    
    
def seatpicked(seatno,seatet):                     #this function is to get wha seats have been picked
    global seatnumber
    global A1,A2,A3,A4,B5,B1,B2,B3,B4,B5,C1,C2,C3,C4,C5
    seatet.configure(state='disabled')
    seatnumber=seatno
    if (seatno not in totalseats):
        totalseats.append(seatno)
    global temp
    global h
    h=[]
    for x in mycursor:
      h.append(list(x))
    m=False
    global seather
    seather+=1
    print(seather,"seatno is",seatnumber)
    if seather==int(jojo):
      after_seat()  

def after_seat():                           #this function is to check for confirmation
    clear2()
    movii=moviename
    if movii=='Gotg':
        movii='GuardiansOfTheGalaxy'
    x.geometry('510x460')
    x.configure(bg='dark slate blue') 
    frr='Seat: '
    switcheroo = {
        "Antman":antman,
        "IronMan":ironman,
        "DoctorStrange":doctorstrange,
        "AvengersEndgame":avengersendgame,
        "BlackPanther":blackpanther,
        "Gotg":gotg,
    }

    for j in range(len(totalseats)):
        frr+=totalseats[j]+" , "
    t1=Label(x,text=frr,bg='dark slate blue',font=('Arial',10,'bold'),fg='gold')
    t2=Label(x,text="Movie: "+movii,bg='dark slate blue',font=('Arial',20,'bold'),fg='gold')
    poop=switcheroo.get(moviename)
    b1=Label(x,image=poop,compound='top',bg='plum1')
    b2=Button(x,text='Proceed to confirmation',command=confirm,font=('Arial',15),bg='plum1',relief='raised')
    b3=Button(x,text='Back',font=('Arial',15),command=lambda: after_login('f'),bg='plum1',relief='raised')
    t2.pack(pady=20,fill='x')
    t1.pack(padx=80,pady=10)
    b1.pack(padx=10,pady=10)
    b2.pack(padx=10,pady=10)
    b3.pack(padx=10,pady=10)   


def confirm():                              #for confirmation
  mycursor.execute("use ooer")
  for i in totalseats:
    print("\n------------------------------------------------------------\n")
    print("username ",kkk)
    print("movie ",moviename)
    print("seatnumber ",i)
    sql = "INSERT INTO "+moviename+" (username, seat) VALUES (%s, %s)"
    val = (kkk, i)
    mycursor.execute(sql, val)
    mydb.commit()
  print("\n------------------------------------------------------------\n")
  cashmoney()
  
  
def cashmoney():                            #this function is for selecting payment method
    clear()
    x.geometry('1200x600')
    x.configure(bg='dark slate blue')
    global payment
    payment=""
    def gg(typer):
        global payment
        if typer=="g":
            print("gpay")
            payment="Google Pay"
            food()
        elif typer=="p":
            print("paytm karo")
            payment="Paytm"
            food()
        elif typer=="c":
            print("cod karo??")
            payment="Cash in booth"
            food()
        else:
            messagebox.showerror(title='Error',message='Fatal error,please tell devs about how you got this error.')
            after_login()

    gpay=PhotoImage(file="gpay1.png")
    cash=PhotoImage(file="cash1.png")
    paytm=PhotoImage(file="paytm1.png")

    gpa=Button(text="Google Pay",image=gpay,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: gg("g"),bg='darkgrey')
    payt=Button(text="Paytm",image=paytm,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: gg("p"),bg='darkgrey')
    co=Button(text="Cash in booth",image=cash,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: gg("c"),bg='darkgrey')
    chhose=Label(x,text='Select a Payment method',font=('Calibri',40,'bold'),bg='dark slate blue',fg='black')

    chhose.grid(row=0,column=0,columnspan=3,padx='300',pady='20',sticky='N')
    gpa.grid(row=1,column=0,padx=5,pady=15)
    payt.grid(row=1,column=1,padx=5,pady=15)
    co.grid(row=1,column=2,padx=5,pady=15)
    x.mainloop()


def food():                                 #this function is for food selection
    clear2()
    whyidk()
    clear()
    mycursor.execute("use food")
    x.configure(bg='dark slate blue')
    x.geometry('1170x600')
    header=Label(x,text=' Select Food',font=("Calibri",40,'bold'),bg="dark slate blue",fg='azure')
    header.grid(row=0,column=0,padx=400,pady=50,sticky='N',columnspan=5)

    vcpop=IntVar(x)
    vcnac=IntVar(x)
    vcbeer=IntVar(x)
    vcdog=IntVar(x)
    vccof=IntVar(x)
    cpop=Checkbutton(x,text='Popcorn',variable=vcpop,onvalue=1,offvalue=0,bg='dark slate blue',fg='azure',selectcolor='black',font=('Arial',15),command=lambda:update('Popcorn'))
    cnac=Checkbutton(x,text='Nachos',variable=vcnac,onvalue=1,offvalue=0,bg='dark slate blue',fg='azure',selectcolor='black',font=('Arial',15),command=lambda:update('Nachos'))
    cdog=Checkbutton(x,text='Hot Dog',variable=vcdog,onvalue=1,offvalue=0,bg='dark slate blue',fg='azure',selectcolor='black',font=('Arial',15),command=lambda:update('Hotdog'))
    cbeer=Checkbutton(x,text='Beer',variable=vcbeer,onvalue=1,offvalue=0,bg='dark slate blue',fg='azure',selectcolor='black',font=('Arial',15),command=lambda:update('Beer'))
    ccof=Checkbutton(x,text='Coffee',variable=vccof,onvalue=1,offvalue=0,bg='dark slate blue',fg='azure',selectcolor='black',font=('Arial',15),command=lambda:update('Coffee'))

    def update(n):
        if n=='Popcorn':
            if vcpop.get()==0:
                opt_pop.configure(state='disabled')
                opt_qpop.configure(state='disabled')
                l1.configure(fg='azure')
            else:
                opt_pop.configure(state='active')
                opt_qpop.configure(state='active')
                l1.configure(fg='yellow')

        elif n=='Nachos':
            if vcnac.get()==0:
                opt_nac.configure(state='disabled')
                opt_qnac.configure(state='disabled')
                l3.configure(fg='azure')
            else:
                opt_nac.configure(state='active')
                opt_qnac.configure(state='active')
                l3.configure(fg='yellow')
                
        elif n=='Beer':
            if vcbeer.get()==0:
                opt_beer.configure(state='disabled')
                opt_qbeer.configure(state='disabled')
                l4.configure(fg='azure')
            else:
                opt_beer.configure(state='active')
                opt_qbeer.configure(state='active')
                l4.configure(fg='yellow')

        elif n=='Hotdog':
            if vcdog.get()==0:
                opt_dog.configure(state='disabled')
                opt_qdog.configure(state='disabled')
                l2.configure(fg='azure')
            else:
                opt_dog.configure(state='active')
                opt_qdog.configure(state='active')
                l2.configure(fg='yellow')

        elif n=='Coffee':
            if vccof.get()==0:
                opt_cof.configure(state='disabled')
                opt_qcof.configure(state='disabled')
                l5.configure(fg='azure')
            else:
                opt_cof.configure(state='active')
                opt_qcof.configure(state='active')
                l5.configure(fg='yellow')

    vopop=StringVar(x)
    vonac=StringVar(x)
    vobeer=StringVar(x)
    vodog=StringVar(x)
    vocof=StringVar(x)

    options1=('Regular','Medium','Large')
    options2=('Regular','Grand Special')
    options3=('Espresso','Cold Coffee','Cappuccino')
    options4=(1,2,3,4)

    qpop=IntVar(x)
    qbeer=IntVar(x)
    qnac=IntVar(x)
    qdog=IntVar(x)
    qcof=IntVar(x)

    qpop.set(options4[0])
    qbeer.set(options4[0])
    qnac.set(options4[0])
    qdog.set(options4[0])
    qcof.set(options4[0])

    opt_qpop=OptionMenu(x,qpop,*options4)
    opt_qnac=OptionMenu(x,qnac,*options4)
    opt_qdog=OptionMenu(x,qdog,*options4)
    opt_qbeer=OptionMenu(x,qbeer,*options4)
    opt_qcof=OptionMenu(x,qcof,*options4)

    vopop.set(options1[0])
    vonac.set(options1[0])
    vodog.set(options2[0])
    vobeer.set(options1[0])
    vocof.set(options3[0])

    opt_pop=OptionMenu(x,vopop,*options1)
    opt_nac=OptionMenu(x,vonac,*options1)
    opt_dog=OptionMenu(x,vodog,*options2)
    opt_beer=OptionMenu(x,vobeer,*options1)
    opt_cof=OptionMenu(x,vocof,*options3)

    opt_qnac.configure(state='disabled')
    opt_qpop.configure(state='disabled')
    opt_qdog.configure(state='disabled')
    opt_qbeer.configure(state='disabled')
    opt_qcof.configure(state='disabled')

    opt_qpop.grid(row=1,column=3,pady=10,sticky='W',padx=10)
    opt_qnac.grid(row=2,column=3,pady=10,sticky='W',padx=10)
    opt_qdog.grid(row=3,column=3,pady=10,sticky='W',padx=10)
    opt_qbeer.grid(row=4,column=3,pady=10,sticky='W',padx=10)
    opt_qcof.grid(row=5,column=3,pady=10,sticky='W',padx=10)

    opt_nac.configure(state='disabled')
    opt_pop.configure(state='disabled')
    opt_dog.configure(state='disabled')
    opt_beer.configure(state='disabled')
    opt_cof.configure(state='disabled')

    cpop.grid(row=1,column=1,pady=10,sticky='E',padx=10)
    cnac.grid(row=2,column=1,pady=10,sticky='E',padx=20)
    cdog.grid(row=3,column=1,pady=10,sticky='E',padx=15)
    cbeer.grid(row=4,column=1,pady=10,sticky='E',padx=30)
    ccof.grid(row=5,column=1,pady=10,sticky='E',padx=20)

    opt_pop.grid(row=1,column=2,pady=10,sticky='W',padx=10)
    opt_nac.grid(row=2,column=2,pady=10,sticky='W',padx=10)
    opt_dog.grid(row=3,column=2,pady=10,sticky='W',padx=10)
    opt_beer.grid(row=4,column=2,pady=10,sticky='W',padx=10)
    opt_cof.grid(row=5,column=2,pady=10,sticky='W',padx=10)
    
    l1=Label(x,text='POPCORN \n R:2000, M:2500, L:2700',bg='dark slate blue',fg='azure',font=('Arial',15))
    l2=Label(x,text='HOT DOG \n R:1000, GS:1500',bg='dark slate blue',fg='azure',font=('Arial',15))
    l3=Label(x,text='NACHOS \n R:3000, M:3500, L:3700',bg='dark slate blue',fg='azure',font=('Arial',15))
    l4=Label(x,text='BEER \n R:300, M:370, L:400',bg='dark slate blue',fg='azure',font=('Arial',15))
    l5=Label(x,text='COFFEE \n E:6000, CC:5500, CP:5700',bg='dark slate blue',fg='azure',font=('Arial',15))
    l6=Label(x,text='Terms and conditions apply',bg='dark slate blue',fg='azure',font=('Arial',10))
    l1.grid(row=1,column=0)
    l2.grid(row=3,column=0)
    l3.grid(row=1,column=4)
    l4.grid(row=3,column=4)
    l5.grid(row=5,column=0)
    l6.grid(row=5,column=4)
    global foodd
    foodd={}
    def submit():
        if vcpop.get()==1:
            foodd['Popcorn']=(vopop.get(),qpop.get())
        else:
            pass

        if vcbeer.get()==1:
            foodd['Beer']=(vobeer.get(),qbeer.get())
        else:
            pass

        if vcdog.get()==1:
            foodd['Hotdog']=(vodog.get(),qdog.get())
        else:
            pass

        if vccof.get()==1:
            foodd['Coffee']=(vocof.get(),qcof.get())
        else:
            pass

        if vcnac.get()==1:
            foodd['Nachos']=(vonac.get(),qnac.get())
        else:
            pass
        global val
        for i in foodd:
            sql = "INSERT INTO "+kkk+" (movie,food,type,quantity) VALUES (%s, %s, %s, %s)"
            val = (moviename,i)+ foodd[i]
            mycursor.execute(sql, val)
            mydb.commit()
        終わり()
    sub=Button(x,text='Submit',bg='plum1',font=('Arial',15),command=submit)
    sub.grid(row=6,column=0,columnspan=5,pady=25)
    

def accessfood():                           #this function is to add money to var batua
    mycursor.execute("use food")
    mycursor.execute("select * from "+kkk+" where movie='%s'"%moviename)
    print("\n"*10)
    myresult = mycursor.fetchall()
    global good
    global foodstring
    good=[]
    for i in myresult:
        good.append(i)
    global batua
    batua=500*len(totalse())
    global foodlist
    for i in good:
      if i[1]=="Popcorn":
          foodlist.append("Popcorn")
          if i[2]=="Regular":
              batua+=2000*i[3]
          if i[2]=="Medium:":
              batua+=2500*i[3]
          if i[2]=="Large":
              batua+=2700*i[3]
      if i[1]=="Nachos":
          foodlist.append("Nachos")
          if i[2]=="Regular":
              batua+=3000*i[3]
          if i[2]=="Medium:":
              batua+=3500*i[3]
          if i[2]=="Large":
              batua+=3700*i[3]
      if i[1]=="Hotdog":
          foodlist.append("Hotdog")
          if i[2]=="Regular":
              batua+=1000*i[3]
          if i[2]=="Grand Special":
              batua+=1500*i[3]
      if i[1]=="Beer":
          foodlist.append("Beer")
          if i[2]=="Regular":
              batua+=300*i[3]
          if i[2]=="Medium:":
              batua+=370*i[3]
          if i[2]=="Large":
              batua+=400*i[3]
      if i[1]=="Coffee":
          foodlist.append("Coffee")
          if i[2]=="Espresso":
              batua+=6000*i[3]
          if i[2]=="Cold Coffee:":
              batua+=5500*i[3]
          if i[2]=="Cappuccino":
              batua+=5700*i[3]
      print("price- ",batua)
      for i in foodlist:
          foodstring+=i


def  終わり():                                 #this is our final function which prints all the information by connecting to sql.
    clear2()    
    accessfood()


    yyy="price- ₹%s"%batua
    x.geometry('1000x670')
    x.configure(bg='dark slate blue') 
    mycursor.execute("use ooer")
    mycursor.execute("select * from "+moviename+" where username='%s'"%kkk)
    myresult = mycursor.fetchall()
    global last
    last=""
    for i in myresult:
      if i!=myresult[-1]:
        last+=i[1]+" , "
      else:
          last+=i[1]

    u="Hey "+kkk+", here's the summary of your booking:"
    m='Movie: '+moviename
    food='Food items: '
    for i in good:
        if i==good[-1]:
            food+=str(i[-1])+" "+i[-2]+" "+i[-3]
        else:
            food+=str(i[-1])+" "+i[-2]+" "+i[-3]+','

    x.geometry('1000x670')
    x.configure(bg='dark slate blue')    
    header=Label(x,text='BOOKING SUMMARY',bg='dark slate blue',fg='firebrick3',font=('Arial',40,'bold'))
    uname=Label(x,text=u,bg='dark slate blue',fg='azure',font=('calibri',20))
    movie=Label(x,text=m,bg='dark slate blue',fg='azure',font=('calibri',20))
    seats=Label(x,text="Seats: "+last,bg='dark slate blue',fg='azure',font=('calibri',20))
    food=Label(x,text=food,bg='dark slate blue',fg='azure',font=('calibri',20))
    cost=Label(x,text="Cost: ₹"+str(batua),bg='dark slate blue',fg='azure',font=('calibri',20))
    pmt=Label(x,text="Payment Method: "+payment,bg='dark slate blue',fg='azure',font=('calibri',20))
    tyn=Label(x,text='Enjoy the movie!',bg='dark slate blue',fg='azure',font=('calibri',25,'bold'))
    btn=Button(x,text='Exit',bg='plum1',command=x.destroy,font=('calibri',20))

    header.pack(pady=20)
    uname.pack(pady=10)
    movie.pack(pady=10)
    seats.pack(pady=10)
    food.pack(pady=10)
    cost.pack(pady=10)
    pmt.pack(pady=10)
    tyn.pack(pady=10)
    btn.pack(ipadx=10,pady=10)
    mydb.close()


x=Tk()
x.geometry('1000x570')
x.configure(bg='dark slate blue')
x.title("Grande Cinema")

header=Label(x,text="Welcome to Grande Cinema",font=("Calibri",40,'bold'),bg='dark slate blue',fg='azure')
header.grid(row=0,column=0,padx='170',pady='90',sticky='N')

s_upbutton=Button(x,text="Sign Up",font=("Arial",15),command=signup,relief='raised',bg='plum1')
s_upbutton.grid(row=1,column=0,pady='40',ipadx='7',ipady='8')

login_button=Button(x,text="Login",font=("Arial",15),command=login,relief='raised',bg='plum1')
login_button.grid(row=2,column=0,ipadx='16',ipady='7')
x.resizable(0,0) # window can't be resized
x.mainloop()

#This is our first sceen