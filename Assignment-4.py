#Q1.Tuples
A=(1,2,3,3,12,32,22)
print(len(A))

#Q2.
print("Maximum element in tuple -",max(A))
print("Minimum element in tuple -",min(A))

#Q3.
S=0
for i in A:
    S=S*i
print("Sum of all elements in tuple -",S)

#Q1.Sets
A={1,2,3,4}
B={2,3}
print("Difference of sets -",A-B)
print("A is superset of B -",A>=B)
print("Intersection of A and B -",A&B)

#Q1.Dictionary
B={}
for i in range(5):
    a=input("Enter name of student %d = " %(i+1))
    b=int(input("Enter marks of student %d = " % (i+1)))
    B[a]=b
print(B)

#Q2.
from collections import OrderedDict
print(OrderedDict(sorted(B.items(),key=lambda t: t[1])))

#Q2..
print(B)
a=sorted(B.values())
print(a)
for v in a:
    for i in B.keys():
        if(B[i]==v):
             print("%s:%d"%(i,v))

#Q3.
l="MISSISSIPPI"
m=l.count("M")
i=l.count("I")
s=l.count("S")
p=l.count("P")
C={}
C["M"]=m
C["I"]=i
C["S"]=s
C["P"]=p
print(C)
