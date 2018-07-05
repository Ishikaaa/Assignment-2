#Q1.
from tkinter import *
a=Tk()
a.title("Ishika Garg")
A = {"Parul": 111, "Ishika Garg": 123, "Anushika Sharma": 234, "Akash kamboj": 345, "Anbay Jindal": 456,"Madhav Ahuja": 567, "Nikhil Sharma": 678, "Sulekha Garg": 789, "Shrishti Gaur": 890}
L3=Label(a,text="")
L3.grid(row=1,column=1)
def show(evt):
    L3.config(text=A[l1.get(l1.curselection())])
L1=Label(a,text="Name:").grid(row=0,column=0)
L2=Label(a,text="Mobile Number:").grid(row=0,column=1)
s1=Scrollbar(a,orient=VERTICAL)
l1=Listbox(a,height=10,yscrollcommand=s1.set)
for i in A.keys():
    l1.insert(END,i)
s1.config(command=l1.yview)
l1.grid(row=1,column=0,rowspan=3)
s1.grid(row=1,column=0,rowspan=3,sticky=E+N+S)
l1.bind("<<ListboxSelect>>",show)
a.mainloop()

#Q2.
from tkinter import *
a=Tk()
a.title("Ishika Garg")
A = {"Parul": 111, "Ishika Garg": 123, "Anushika Sharma": 234, "Akash kamboj": 345, "Anbay Jindal": 456,"Madhav Ahuja": 567, "Nikhil Sharma": 678, "Sulekha Garg": 789, "Shrishti Gaur": 890}
x=StringVar()
y=IntVar()
L3=Label(a,text="")
L3.grid(row=1,column=1)
def show(evt):
    L3.config(text=A[l1.get(l1.curselection())])
def show1():
    A[x.get()]=y.get()
    aaaa=x.get()
    l1.insert(END, aaaa)
    show3()
L1=Label(a,text="Name:").grid(row=0,column=0)
L2=Label(a,text="Mobile Number:").grid(row=0,column=1)
s1=Scrollbar(a,orient=VERTICAL)
l1=Listbox(a,height=10)
def show3():
    s1.config(command=l1.yview)
    s1.grid(row=1, column=1, rowspan=3, sticky=W, ipady=60)
    l1.grid(row=1, column=0, rowspan=1)
    l1.bind("<<ListboxSelect>>", show)
for i in A.keys():
        l1.insert(END, i)
        show3()
l4=Label(a,text="enter name=").grid(row=4,column=0)
l5=Label(a,text="Enter mobile number=").grid(row=4,column=1)
e1=Entry(a,textvariable=x).grid(row=5,column=0)
e2=Entry(a,textvariable=y).grid(row=5,column=1)
b1=Button(a,text="Refresh",command=show1).grid(row=6)
a.mainloop()