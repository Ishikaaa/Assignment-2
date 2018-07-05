#Q1.
from tkinter import *
a=Tk()
a.title("Ishika Garg")
l=Label(a,text="Helo World").pack()
b=Button(a,text="Exit",command=quit).pack()
a.mainloop()

#Q2.
from tkinter import *
a=Tk()
a.title("Ishika Garg")
def show():
    print("Hello World")
    l=Label(a,text="Hello World").pack()
b1=Button(a,text="Click",command=show).pack()
b2=Button(a,text="Stop",command=a.destroy).pack()
a.mainloop()

#Q3.
from tkinter import *
a=Tk()
a.title("Ishika Garg")
l1=Label(a,text="Before Clicking Button")
l1.grid(row=0,sticky=W)
def show():
    l1.config(text="After Clicking Button")
ishika=1
b1=Button(a,text="Click",command=show)
b1.grid(row=1)
b2=Button(a,text="Exit",command=a.destroy)
b2.grid(row=2)
a.mainloop()

#Q4.
from tkinter import *
a=Tk()
def show():
    ee=v1.get()
    l=Label(a,text=ee).grid(row=2)
v1=IntVar()
a.title("Ishika Garg")
b=Button(a,text="Click",command=show).grid(row=1)
e=Entry(a,textvariable=v1).grid(row=0)
a.mainloop()


