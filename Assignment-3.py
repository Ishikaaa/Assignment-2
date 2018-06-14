#Q1.
a=[]
b=input("Enter any number=")
a.append(b)
print(a)

#Q2.
a=[1,2]
a.append(['google','apple','facebook','microsoft','tesla'])
print(a)

#Q3.
b=[1,3,2,3,4,3]
print(b.count(3))

#Q4.
c=[4,3,1,5,3,2,34]
c.sort()
print(c)

#Q5.
A=[3,2,1,4]
A.sort()
B=[7,5,4,5,0]
B.sort()
C=A+B
C.sort()
print("Sorted merge list is -",C)

#Q6.
D=[2,1,3,4,2]
print("Implementation of stack--")
print(D)
D.append(9)
print(D)
D.pop()
print(D)
print("1.Implementation of queue--")
print(D)
D.append(10)
print(D)
D.pop(0)
print(D)

from collections import deque
queue = deque([1,2,3,4])
print("2.implementation of queue--")
print(queue)
queue.append(5)
print(queue)
queue.popleft()
print(queue)

#Q7.
X=[1,3,2,6,5,12,43,33]
oo=0
ee=0
for i in X:
    if(i%2==0):
        ee+=1
    else:
        oo+=1
print("Odd elements in list -",oo)
print("Even elements in list -",ee)

