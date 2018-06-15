#1.class notes
print(" There are 2 kinda of data types- mutable(which can change)Foreg - List,dictionary and immutable(which can not be change..Foreg-String,tuple")

'''#2. number data type
a=1
b=1.1
c=1+3j
print(type(a))
print(type(b))
print(type(c))
print(isinstance(a,int))#This ensure that python is object oriented programming.
print(isinstance(b,float))
print(isinstance(c,int))
'''

'''
#3. string data type
a="Hello"
a[2]='b'# we can not replace some characters of string
print(a)
'''

'''
#3. String data type
a="hello"
print(a[-1])
b="Ishika Garg9"
#b.(nowpress ctrl+space)
print(b.upper())
print(len(b))
print(b.capitalize())#self means it doesn't accept any more parameter.
print(b.isalpha())#when is come in beginning then that method checks something and give answer in True and False
print(a.isalpha())


#4. list data type[]..We can write multiple data types in list.
a=[1,[1,2,3],"Hello"]
print(a[-2])
print(a[1][1])
b=[1,2,3,4,5]
print(a.pop())#stack
a.append(b)#stack. For queue , use deque method
print(b)
b.insert(1,3)
print(b)
b.reverse()
print(b)
b.sort()
print(b)
print(b.count(3))
'''

a=[6,8,9]
a.pop(1)
print(a)