#Q1.
l=[]
for i in range(10):
    a=int(input("Enter number ="))
    l.append(a)
print(l)

# # Q2.
# while(True):
#     print("Infinte loop")

#Q3.
l=[]
s=[]
for i in range(5):
    a=int(input("Enter number="))
    l.append(a)
print("Original list l is",l)
for j in l:
    b=j*j
    s.append(b)
print("Square of elements of list l is",s)

#Q4.
from random import shuffle
A=[]
I=[]
F=[]
S=[]
for i in range(2):
    a=int(input("Enter integer="))
    A.append(a)
    b=float(input("Enter float="))
    A.append(b)
    c=str(input("Enter string="))
    A.append(c)
shuffle(A)
print("List is -",A)
for i in A:
    if(type(i) is int):
        I.append(i)
    elif(type(i) is float):
        F.append(i)
    else:
        S.append(i)
print("Integer list is -",I)
print("Float list is -",F)
print("String list is -",S)

#Q5.
e=[]
o=[]
for i in range(1,101):
    if (i%2==0):
        e.append(i)
    else:
        o.append(i)
print("Even list is",e)
print("Odd list is",o)

#Q6.
for i in range(5):
    print("")
    for j in range(i):
        print("* ",end="")

#Q7.
A={"a":1,"b":2,"c":3,"d":4}
for i in A.values():
    for j in A.keys():
        if(i==A[j]):
            print("value =",i,"corresponding to key =",j)

#Q8.
A=[]
c=0
for i in range(5):
    a=int(input("Enter values="))
    A.append(a)
print("List is -",A)
w=int(input("Enter number that you want to find="))
for j in A:
    if(j==w):
        print(w,"found at",j,"position")
        A.remove(j)
        c=1
if(c==1):
    print("Remaining list is -",A)
else:
    print(w,"is not found in list")