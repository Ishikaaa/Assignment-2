#Q1.
print("Time tuple is used to represen time in a way it is easy to understand.And it is stored in tuple.And also that these tuples aree made of nine numbers..\neg:index:0->year...index:1->Month...index:2->Day...index:3->hour...index:4->Minute..index:5->Sec..index:6->Day of Week..index:7->day f year..index:8->Dst")

#Q2.
import time
print(time.strftime("%H:%M:%S"))

#Q3.Extract month from time
import time
print(time.strftime("%b"))

#Q4.
import time
print(time.strftime("%d"))
print(time.strftime("%A"))

#Q5.
import datetime
year=int(input("Enter year="))
mon=int(input("Enter month="))
date=int(input("Enter date="))
date1=datetime.date(year,mon,date)
print(date1)
print(date1.strftime("%b"))

#Q6.
import time,datetime
a=time.localtime()
print(a)
print("Time using localtime-%d:%d:%d"%(a[3],a[4],a[5]))

#Q7.
import math
a=int(input('Enter a number='))
print(math.factorial(a))

#Q9.
import os
print("current working dirfectory -",os.getcwd())
print("environment -",os.environ)
