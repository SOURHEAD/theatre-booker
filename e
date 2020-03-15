from tkinter import *
from tkinter.ttk import *
import mysql.connector

def mysqldb():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="amity"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
      print(x)


root = Tk() 
x=root

x.configure(bg="light green")
x.title("Computer Science")


def click():
    e = textentry.get()
    Label(x,text=e).pack()
    
textentry=Entry(x,width=10)
textentry.grid(row=1,column=0)
textentry.insert(0,"here")

Button(x,text="soobmit",width=6,command=click).grid(row=2 , column=0)
  
# Creating a photoimage object to use image 
photo = PhotoImage(file = r"C:\\Users\\arnav\\OneDrive\\Desktop\\al co..png") 

i=0

if(i<9):
    for i in range(10):
        Label(root, image = photo).grid(row=0,column=0)
        print(i)

if(i==9):
    x.configure(bg="light blue" )
    DestroyTest(root)

x.mainloop() 
