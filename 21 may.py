from tkinter import *
from tkinter import messagebox

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="amity",
  database="ooer"
)

mycursor = mydb.cursor()

l=[]
mycursor.execute("SHOW TABLES")
for x in mycursor:
  l.append(x)
he=[]
for i in l:
    he.append(list(i))
 
me=False
for i in he:
    if "profile" in i:
        me=True
        break
    
if me:
  pass
else:
  mycursor.execute("create table profile (username varchar(255) PRIMARY KEY, password varchar(255) NOT NULL)")

username=password=0


def createtables():
    for i in povies:
       if i in h:
           continue
       else:
           mycursor.execute("create table %s (seat varchar(255) PRIMARY KEY, username varchar(255))" %i) 
           mydb.commit()
povies=['blackpanther','antman','ironman','doctorstrange','avengersendgame','gotg']
mycursor.execute("show tables")
h=[]
for x in mycursor:
  h.append(x[0])

createtables()

def seats():
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
seats()

def seatpicked(seatno):
    global seatnumber
    seatnumber=seatno
    print("username ",kkk)
    print("movie ",moviename)
    print("seatnumber ",seatnumber)
    global temp
    temp={'username':kkk,'movie':moviename,'seatnumber':seatnumber}
    after_seat()

def after_seat():
    clear2()
    movii=moviename
    if movii=='Gotg':
        movii='GuardiansOfTheGalaxy'
    x.geometry('510x420')
    x.configure(bg='dark slate blue') 
    pop=PhotoImage(file='pop.png')
    t1=Label(x,text='Seat: '+seatnumber,bg='dark slate blue',font=('Arial',20,'bold'),fg='gold')
    t2=Label(x,text="Movie: "+movii,bg='dark slate blue',font=('Arial',20,'bold'),fg='gold')
    b1=Button(x,text="Khaana?",command=food,image=pop,compound='top',bg='plum1',font=('Arial',15),relief='raised')
    b1.image=pop
    b2=Button(x,text='No,proceed to confirmation',command=confirm,font=('Arial',15),bg='plum1',relief='raised')
    b3=Button(x,text='Back',font=('Arial',15),command=lambda: after_login('f'),bg='plum1',relief='raised')
    t2.pack(pady=20,fill='x')
    t1.pack(padx=80,pady=10)
    b1.pack(padx=10,pady=10)
    b2.pack(padx=10,pady=10)
    b3.pack(padx=10,pady=10)
    
def food():
    print('food')

def confirm():
    print('confirm')
      
def moviesseatelection():
     clear2()
     x.geometry('636x610')
     x.configure(bg='dark slate blue')
     scr=Label(x,text='SCREEN HERE',fg='black',bg='lavender',font=('Arial',30,'bold')).grid(row=0,column=1,columnspan=5,ipadx=110,padx=50,pady=80)
     seata1=Button(text="A1",command=lambda: seatpicked('A1'),bg="lightgreen",font=('Arial',15),relief='raised')
     seata2=Button(text="A2",command=lambda: seatpicked('A2'),bg="lightgreen",font=('Arial',15),relief='raised')
     seata3=Button(text="A3",command=lambda: seatpicked('A3'),bg="lightgreen",font=('Arial',15),relief='raised')
     seata4=Button(text="A4",command=lambda: seatpicked('A4'),bg="lightgreen",font=('Arial',15),relief='raised')
     seata5=Button(text="A5",command=lambda: seatpicked('A5'),bg="lightgreen",font=('Arial',15),relief='raised')
     seatb1=Button(text="B1",command=lambda: seatpicked('B1'),bg="lightgreen",font=('Arial',15),relief='raised')
     seatb2=Button(text="B2",command=lambda: seatpicked('B2'),bg="lightgreen",font=('Arial',15),relief='raised')
     seatb3=Button(text="B3",command=lambda: seatpicked('B3'),bg="lightgreen",font=('Arial',15),relief='raised')
     seatb4=Button(text="B4",command=lambda: seatpicked('B4'),bg="lightgreen",font=('Arial',15),relief='raised')
     seatb5=Button(text="B5",command=lambda: seatpicked('B5'),bg="lightgreen",font=('Arial',15),relief='raised')
     seatc1=Button(text="C1",command=lambda: seatpicked('C1'),bg="lightgreen",font=('Arial',15),relief='raised')
     seatc2=Button(text="C2",command=lambda: seatpicked('C2'),bg="lightgreen",font=('Arial',15),relief='raised')
     seatc3=Button(text="C3",command=lambda: seatpicked('C3'),bg="lightgreen",font=('Arial',15),relief='raised')
     seatc4=Button(text="C4",command=lambda: seatpicked('C4'),bg="lightgreen",font=('Arial',15),relief='raised')
     seatc5=Button(text="C5",command=lambda: seatpicked('C5'),bg="lightgreen",font=('Arial',15),relief='raised')
     backer=Button(text="Back",command=after_login,bg="azure",font=('Arial',15))
     seata1.grid(row=1,column=1,ipadx=15,ipady=15,pady=10)
     seata2.grid(row=1,column=2,ipadx=15,ipady=15,pady=10)
     seata3.grid(row=1,column=3,ipadx=15,ipady=15,pady=10)
     seata4.grid(row=1,column=4,ipadx=15,ipady=15,pady=10)
     seata5.grid(row=1,column=5,ipadx=15,ipady=15,pady=10)
     seatb1.grid(row=2,column=1,ipadx=15,ipady=15,pady=10)
     seatb2.grid(row=2,column=2,ipadx=15,ipady=15,pady=10)
     seatb3.grid(row=2,column=3,ipadx=15,ipady=15,pady=10)
     seatb4.grid(row=2,column=4,ipadx=15,ipady=15,pady=10)
     seatb5.grid(row=2,column=5,ipadx=15,ipady=15,pady=10)
     seatc1.grid(row=3,column=1,ipadx=15,ipady=15,pady=10)
     seatc2.grid(row=3,column=2,ipadx=15,ipady=15,pady=10)
     seatc3.grid(row=3,column=3,ipadx=15,ipady=15,pady=10)
     seatc4.grid(row=3,column=4,ipadx=15,ipady=15,pady=10)
     seatc5.grid(row=3,column=5,ipadx=15,ipady=15,pady=10)
     backer.grid(row=4,column=1,columnspan=5,pady=45)
     x.mainloop() 

def intr():
    x=Tk()
    photo = PhotoImage(file = "cs.png")
    x.title("Welcome to Grande Cinema!")
    x.geometry('1280x720')
    
    a=Label(x, image = photo)
    a.grid(row=0)
    a.after(3000 , a.master.destroy)
    x.mainloop()
 
#intr()

x=Tk()
x.geometry('1000x570')
x.configure(bg='dark slate blue')
x.title("Grande Cinema")

def enter_into_table():
    try:
        sql = "INSERT INTO profile (username,password) VALUES (%s, %s)"
        val = (kkk,ull )
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo(message='Account Created!')
        login()
    except:
        messagebox.showerror(title='Error',message='Username not available')
    
def clear2():
    list = x.grid_slaves()
    for l in list:
        l.destroy()

def clear():
    list = x.pack_slaves()
    for l in list:
        l.destroy()

def new_ac():
    global kkk
    global ull
    kkk=username.get()
    ull=password.get()
    enter_into_table()

def cl():
    global kkk
    global ull
    global trodo
    kkk=username.get()
    ull=password.get()
    
    mycursor.execute("SELECT * FROM profile")
    myresult = mycursor.fetchall()
    for i in myresult:
        if (kkk,ull)==i:
            after_login()
            break
    else:
        messagebox.showerror(title='Error',message='Invalid Username/Password. Try again')
        
def signup():
    clear2()
    x.configure(bg="dark slate blue")
    x.geometry("1000x570")
    
    t1=Label(text="SIGN UP",font=("Arial",40,'bold'),bg="dark slate blue",fg='azure')
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
    
def login():
    clear2()
    x.configure(bg="dark slate blue")
    x.geometry("1000x570")
    
    t2=Label(text="LOGIN",font=("Arial",40,'bold'),bg="dark slate blue",fg='azure')
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

def after_login(a=''):
    if a=='f':
        clear()
        a=''
    else:
        clear2()
    x.configure(bg="gray10")
    x.geometry("1000x650")
    
    header=Label(x,text='Select a movie',font=('Calibri',40,'bold'),bg='gray10',fg='SlateGray3')
    header.grid(row=0,column=0,columnspan=3,padx='300',pady='20',sticky='N')
    
    Antman=PhotoImage(file='Antman.png')
    IronMan=PhotoImage(file='IronMan.png')
    DoctorStrange=PhotoImage(file='DoctorStrange.png')
    AvengersEndgame=PhotoImage(file='AvengersEndgame.png')
    BlackPanther=PhotoImage(file='BlackPanther.png')
    Gotg=PhotoImage(file='Gotg.png')
    
    b1=Button(x, text='Black Panther',image=BlackPanther,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('Black Panther'),bg='gold')
    b2=Button(x, text='Antman',image=Antman,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('Antman'),bg='gold')
    b3=Button(x, text='IronMan',image=IronMan,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('Iron Man'),bg='gold')
    b4=Button(x, text='Doctor Strange',image=DoctorStrange,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('Doctor Strange'),bg='gold')
    b5=Button(x, text='Avengers\nEndgame',image=AvengersEndgame,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('Avengers Endgame'),bg='gold')
    b6=Button(x, text='Guardians Of\nThe Galaxy',image=Gotg,cursor='circle',compound='top',font=('Calibri',15),fg='black',command=lambda: select_movie('Gotg'),bg='gold')
    
    b1.grid(row=1,column=0,padx=5,pady=15)
    b2.grid(row=1,column=1,padx=5,pady=15)
    b3.grid(row=1,column=2,padx=5,pady=15)
    b4.grid(row=2,column=0,padx=5,pady=15)
    b5.grid(row=2,column=1,padx=5,pady=15)
    b6.grid(row=2,column=2,padx=5,pady=15)
    x.mainloop()

def select_movie(name):
    clear2()
    x.configure(bg='dark slate blue')
    x.geometry('250x400')
    global moviename
    moviename=""
    for i in name:
        if i.isalpha():
            moviename+=i
    loc=moviename+".png"
    img=PhotoImage(file=loc)
    center=Label(x,text=name,image=img,compound='top',font=('Calibri',15),fg='black',bg='gold')
    center.image=img
    center.grid(row=1,column=0,padx='55',pady='40')
    Button(x,text='Back',font=('Arial'),command=after_login,bg='plum1').grid(row=3,column=0,pady=10)
    Button(x,text='Select Seats',font=('Arial'),command=moviesseatelection,bg='plum1').grid(row=2,column=0)

header=Label(x,text="Welcome to Grande Cinema",font=("Calibri",40,'bold'),bg='dark slate blue',fg='azure')
header.grid(row=0,column=0,padx='170',pady='90',sticky='N')

s_upbutton=Button(x,text="Sign Up",font=("Arial",15),command=signup,relief='raised',bg='plum1')
s_upbutton.grid(row=1,column=0,pady='40',ipadx='7',ipady='8')

login_button=Button(x,text="Login",font=("Arial",15),command=login,relief='raised',bg='plum1')
login_button.grid(row=2,column=0,ipadx='16',ipady='7')
x.resizable(0,0)
x.mainloop()