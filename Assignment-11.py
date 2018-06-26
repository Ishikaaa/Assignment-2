#Q1.
import time
import threading
class Mymy(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print("Hiiii! Threading here")
T1=Mymy()
time.sleep(5)
T1.start()

#Q2.
import time
import threading
class Mymymy(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,11):
            print(i)
            time.sleep(1)
T2=Mymymy()
T2.start()

#Q3.
import time
import threading
class Mymymymy(threading.Thread):
    def __init__(self,l,t):
        threading.Thread.__init__(self)
        self.l=l
        self.t=t
    def run(self):
        for i,j in zip(l,t):
            time.sleep(j)
            print(i)
l=[1,2,3,4,5]
t=[2,4,6,8,10]
T3=Mymymymy(l,t)
T3.start()

#Q3.....
import time
import threading
class Mymymymy(threading.Thread):
    def __init__(self,l,t):
        threading.Thread.__init__(self)
        self.l=l
        self.t=t
    def run(self):
        global j
        for i in self.l:
            for j in range(5):
                time.sleep(t[j])
                print(i)
                self.t.remove(self.t[0])
                break
l=[1,2,3,4,5]
t=[2,4,6,8,10]
T3=Mymymymy(l,t)
T3.start()

#Q4.
import time
import threading
import math
class Mymy1(threading.Thread):
    def __init__(self,a):
        threading.Thread.__init__(self)
        self.a=a
    def run(self):
        print("factorial of %d = %d"%(self.a,math.factorial(self.a)))
a=int(input("Enter number="))
TT=Mymy1(a)
TT.start()

