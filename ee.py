# #1. lambda expression or anonymous function
# g=lambda x:3*x+1
# print(g(3))

# #2.To add elements in tuple
# a = ('2')
# items = ['o', 'k', 'd', 'o']
# l = list(a)
# for x in items:
#     l.append(x)
# print (tuple(l))

# a = ('x', 'y')
# b = a + ('z',)
# print(b)

# a = ('x', 'y')
# b = a + tuple('b')
# print(b)
#
# a=(1,2)
# b=(3,4)
# c=a+b
# print(c)

# a = ('2',)
# b = 'z'
# new = a + (b,)
# print(new)

# A={"a":3,"b":1,"c":2,"x":0,"z":10}
# a=sorted(A.values())
# print(a)
# for key in sorted(A):
#     print("%s:%d"%(key,A[key]))
#     sorted(A.keys())

# A={"a":3,"b":1,"c":2,"x":0,"z":10}
# sorted([(value,key) for (key,value) in A.items()])
# print(A)
#
# A={"a":3,"b":1,"c":2,"x":0,"z":10}
# for key in sorted(A.iterkeys()):
#     print ("%s: %s" % (key, A[key]))

# A={"a":3,"b":1,"c":2,"x":0,"z":10}
# keylist = A.values()
# keylist.sort()
# for key in keylist:
#     print ("%s: %s" % (key, A[key]))
# A = {"a": 3, "b": 1, "c": 2, "x": 0, "z": 10}
# for key in sorted(A):
# print("%s: %s" % (key, A[key]))
# sort(dict.keys())

A={"a":1,"b":3,"c":2,"x":0,"z":10}
print(A)
a=sorted(A.values())
print(a)
for v in a:
    for i in A.keys():
        if(A[i]==v):
             print("%s:%d"%(i,v))


# A={"a":1,"b":3,"c":2,"x":0,"z":10}
# a=sorted(A.values())
# print(a)
# for v in a:
#     for i in A.keys():
#         if(A[i]==v):
#              kk=i
#              vv=v
#              print()
# print(A)