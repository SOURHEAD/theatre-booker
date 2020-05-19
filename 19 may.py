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
  print(x)
  l.append(x)
loool=False
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

def intr():
    x=Tk()
    photo = PhotoImage(file = "cs.png")
    x.title("Welcome to Grande Cinema!")
    x.geometry('1280x720')
    a=Label(x, image = photo)
    a.grid(row=0)
    a.after(3000 , a.master.destroy)
    x.mainloop()
 
intr()


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
    trodo=[]
    p=[]
    for i in myresult:
        trodo.append(i)
    for i in trodo:
        p.append(list(i))
    global meh
    meh=False
    for i in p:
          if i[0]==kkk:
            meh=True
            break
          else:
            continue
    if (not meh):
        print("wrong username")
    else:
        print("password likhna he ab")

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
    u_label=Label(x,text="Enter Username",font=('Calibri',20),bg='dark slate blue',fg='azure')
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
    submit_btn=Button(text="Proceed",command=cl,font=('Arial',15),bg='plum1',relief='raised')
    submit_btn.grid(row=3,column=0,padx=20,pady=60,sticky='E')
    but2=Button(text="Don't have an account? Sign up!",command=signup,font=('Arial',15),bg='plum1',relief='raised')
    but2.grid(row=3,column=1,padx=20,pady=60,sticky='W')
    x.mainloop()

header=Label(x,text="Welcome to Grande Cinema",font=("Calibri",40,'bold'),bg='dark slate blue',fg='azure')
header.grid(row=0,column=0,padx='170',pady='90',sticky='N')
s_upbutton=Button(x,text="Sign Up",font=("Arial",15),command=signup,relief='raised',bg='plum1')
s_upbutton.grid(row=1,column=0,pady='40',ipadx='7',ipady='8')
login_button=Button(x,text="Login",font=("Arial",15),command=login,relief='raised',bg='plum1')
login_button.grid(row=2,column=0,ipadx='16',ipady='7')

x.mainloop()
