# #1.If you want to add more than one numbers at one time
# A=[1,2]
# for i in range(4):
#     a=int(input("Enter nunmber="))
#     A.append(a)
# print(A)
#
#
# A=[1,2]
# a=int(input("Enter 1st number="))
# b=int(input("Enter 2nd number="))
# c=int(input("Enter 3rd number="))
# d=int(input("Enter 4th number="))
# A.extend([a,b,c,d])
# print(A)

#2. Implementation of queue
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print("implementation of queue(2nd method)--")
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

from collections import bb
A=bb([1,2,3,4])
print(A)
A.append(10)
print(A)
print(A.popleft())

from collections import *deque
A=[1,2,3,4]
print(A)
A.append(10)
print(A)
print(A.popleft())

#3.How to sort a list in descending order without using reverse function
a=[1,2,3]
