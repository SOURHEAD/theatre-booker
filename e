from tkinter import *

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


tentry=tentre=0

def intr():
 x=Tk()
 photo = PhotoImage(file = "cs.png")
 x.title("Intro")
 a=Label(x, image = photo)
 a.grid(row=0)
 a.after(5000 , a.master.destroy)
 x.mainloop()

intr()


x=Tk()
x.geometry('1280x1024')
x.configure(bg="lightyellow")
x.title("account")

def gamer():
    sql = "INSERT INTO profile (username,password) VALUES (%s, %s)"
    val = (kkk,ull )
    mycursor.execute(sql, val)

    mydb.commit()

def clear():
    list = x.pack_slaves()
    for l in list:
        l.destroy()
def clear2():
    list = x.grid_slaves()
    for l in list:
        l.destroy()

def click():
    global kkk
    global ull
    kkk=tentry.get()
    ull=tentre.get()
    gamer()

def cl():
    global kkk
    global ull
    global trodo
    kkk=tentry.get()
    ull=tentre.get()
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
    loool=True
    clear()
    x.configure(bg="lightblue")
    x.geometry("600x300")
    Label(text="Please enter the following - ",font=("Comic Sans MS",15),bg="lightblue").grid(row=0,column=0)
    Labil=Label(x,text="",width=10,height=4,bg="lightblue")
    Labil.grid(row=1,column=1)
    Label(x,text="Please enter a username - ").grid(row=2,column=0)
    global tentry
    global tentre
    tentry=Entry(x,text="Plese enter username here")
    tentry.grid(row=2,column=1)
    Labil=Label(x,text="",width=10,height=2,bg="lightblue")
    Labil.grid(row=3,column=0)
    Label(x,text="Please enter a password - ").grid(row=4,column=0)
    tentre=Entry(x,text="Plese enter password here")
    tentre.config(show="*") 
    tentre.grid(row=4,column=1)
    but1=Button(text="Submit",command=click)
    Labirl=Label(x,text="",width=10,height=4,bg="lightblue")
    Labirl.grid(row=5,column=0)
    but1.grid(row=6,column=0)
    but2=Button(text="Click here to go back to login",command=login)
    but2.grid(row=6,column=1)
    x.mainloop()
    
def login():
    if loool:
        clear2()
    else:
        clear()
    x.configure(bg="lightblue")
    x.geometry("600x300")
    Label(text="Please enter the following - ",font=("Comic Sans MS",15),bg="lightblue").grid(row=0,column=0)
    Labil=Label(x,text="",width=10,height=4,bg="lightblue")
    Labil.grid(row=1,column=1)
    Label(x,text="Please enter your username - ").grid(row=2,column=0)
    global tentry
    global tentre
    tentry=Entry(x,text="username ")
    tentry.grid(row=2,column=1)
    Labil=Label(x,text="",width=10,height=2,bg="lightblue")
    Labil.grid(row=3,column=0)
    Label(x,text="Please enter your password - ").grid(row=4,column=0)
    tentre=Entry(x,text="password")
    tentre.config(show="*") 
    tentre.grid(row=4,column=1)
    but1=Button(text="Submit",command=cl)
    Labirl=Label(x,text="",width=10,height=4,bg="lightblue")
    Labirl.grid(row=5,column=0)
    but1.grid(row=6,column=0)
    but2=Button(text="Need to sign up?",command=signup)
    but2.grid(row=6,column=1)
    x.mainloop()

Label(x,text="Please do either of the following -",font=("Arial Black",30),fg="Black",anchor=W).pack()
Labil=Label(x,text="",width=10,height=20,bg="lightyellow")
Labil.pack()
Button(x,text="Sign Up",font="Impact",width=10,height=3,relief="raised",command=signup).pack()
Label(x,text="",width=10,height=8,bg="lightyellow").pack()
Button(x,text="Login",font="Impact",width=10,height=3,relief="raised",command=login).pack()

x.mainloop()
