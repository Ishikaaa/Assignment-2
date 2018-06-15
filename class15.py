# print("Advantages of tuple- 1.")
# #1.methods in tuple. We can not use append and pop in tuple
# A=(1,2,3)
# print(A)
# print(A[1:2])
# print(len(A))
# print(list(A))
# L=[33,44,22,1]
# DD=tuple(L)
# print(DD)
# del DD
# print(DD)

# #2. Set
# A=set([1,2,3])
# B=set((3,4,5))
# print("Inetrsection -",A&B)# intersection
# print("Union -",A|B)#union
# C=set()
# C.add(1)
# print(C)
# C.add(2)
# print(C)
# C.update(set([1,2,3,44,11]))
# print(C)
# C.pop()
# print(C)
# C.remove(11)
# print(C)
# C.discard(9)# it does not show error if wrong parameter is used
# print(C)

# #2.
# A={1,2,3,4}
# B={2,4}
# print("A is subset of B -",A>=B)
# print("B is subset of A -",B<=A)

#3. Dictionary
D={"name":"Ishika Garg","age":19}
print(D)
print(D["name"])
D["name"]="Ishika"
print(D)# so dictionary is mutable

#Dictionary functions
del D["name"]
print(D)
D.clear()
print(D)

A={1:5,3:[11,1,33,12]}
print(A)
del A[3][0]
print(A)