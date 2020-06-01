from tkinter import *

x=Tk()
x.configure(bg='dark slate blue')
x.geometry('1000x600')

header=Label(x,text='Khaana',font=("Calibri",40,'bold'),bg="dark slate blue",fg='azure')
header.grid(row=0,column=0,padx=400,pady=50,sticky='N',columnspan=5)

vcpop=IntVar(x)
vcnac=IntVar(x)
vcbeer=IntVar(x)
vcdog=IntVar(x)
vccof=IntVar(x)

cpop=Checkbutton(x,text='Popcorn',variable=vcpop,onvalue=1,offvalue=0,bg='dark slate blue',fg='azure',selectcolor='black',font=('Arial',15),command=lambda:update('pop'))
cnac=Checkbutton(x,text='Nachos',variable=vcnac,onvalue=1,offvalue=0,bg='dark slate blue',fg='azure',selectcolor='black',font=('Arial',15),command=lambda:update('nac'))
cdog=Checkbutton(x,text='Hot Dog',variable=vcdog,onvalue=1,offvalue=0,bg='dark slate blue',fg='azure',selectcolor='black',font=('Arial',15),command=lambda:update('dog'))
cbeer=Checkbutton(x,text='Beer',variable=vcbeer,onvalue=1,offvalue=0,bg='dark slate blue',fg='azure',selectcolor='black',font=('Arial',15),command=lambda:update('beer'))
ccof=Checkbutton(x,text='Coffee',variable=vccof,onvalue=1,offvalue=0,bg='dark slate blue',fg='azure',selectcolor='black',font=('Arial',15),command=lambda:update('cof'))

def update(n):
    if n=='pop':
        if vcpop.get()==0:
            opt_pop.configure(state='disabled')
            opt_qpop.configure(state='disabled')
        else:
            opt_pop.configure(state='active')
            opt_qpop.configure(state='active')
                             
    elif n=='nac':
        if vcnac.get()==0:
            opt_nac.configure(state='disabled')
            opt_qnac.configure(state='disabled')
        else:
            opt_nac.configure(state='active')
            opt_qnac.configure(state='active')
                               
    elif n=='beer':
        if vcbeer.get()==0:
            opt_beer.configure(state='disabled')
            opt_qbeer.configure(state='disabled')
        else:
            opt_beer.configure(state='active')
            opt_qbeer.configure(state='active')
                                
    elif n=='dog':
        if vcdog.get()==0:
            opt_dog.configure(state='disabled')
            opt_qdog.configure(state='disabled')
        else:
            opt_dog.configure(state='active')
            opt_qdog.configure(state='active')
                               
    elif n=='cof':
        if vccof.get()==0:
            opt_cof.configure(state='disabled')
            opt_qcof.configure(state='disabled')
        else:
            opt_cof.configure(state='active')
            opt_qcof.configure(state='active')
     
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

img1=PhotoImage(file='nachos.png')
img3=PhotoImage(file='beer.png')

l1=Label(x,image=img1,bg='dark slate blue')
l3=Label(x,image=img3,bg='dark slate blue')

l1.grid(row=1,column=0,rowspan=4)
l3.grid(row=1,column=4,rowspan=4)

def submit():
    global food
    food={}
    
    if vcpop.get()==1:
        food['pop']=(vopop.get(),qpop.get())
    else:
        pass
    
    if vcbeer.get()==1:
        food['beer']=(vobeer.get(),qbeer.get())
    else:
        pass
    
    if vcdog.get()==1:
        food['dog']=(vodog.get(),qdog.get())
    else:
        pass
    
    if vccof.get()==1:
        food['cof']=(vocof.get(),qcof.get())
    else:
        pass
    
    if vcnac.get()==1:
        food['nac']=(vonac.get(),qnac.get())
    else:
        pass
    
sub=Button(x,text='Submit',bg='plum1',font=('Arial',15),command=submit)
sub.grid(row=6,column=0,columnspan=5,pady=25)

x.mainloop()

