#Q1.
a=open("Ishika_Garg.txt","r",encoding="utf8")
for line in reversed(list(open("Ishika_Garg.txt","r",encoding="utf8"))):
    print(line.rstrip())
n=int(input("Enter lines to be read="))
a=open("Ishika_Garg.txt","r",encoding="utf8")
lines=a.readlines()
print(lines[0:n-1])

#Q2.
a=input("Enter word that you want to search=")
c=0
with open("Ishika_Garg.txt","r",encoding="utf8") as f:
    for line in f:
        b=line.split()
        for i in b:
            if(i==a):
                c+=1
if(c!=0):
    print('"%s" occur %d times'%(a,c))
else:
    print('"%s" does not exist'%a)


#Q3.
with open("Ishika_Garg.txt","r",encoding="UTF-8") as f:
    with open("Ishika_Garg2.txt","w",encoding="UTF-8") as ff:
        ff.write("Ishika Grag")
        for i in f:
            ff.write(i)

#Q4.
with open("Ishika_Garg.txt","r",encoding="UTF-8" ) as f:
    with open("Ishika_Garg2.txt", "r", encoding="UTF-8") as f2:
        with open("Ishika_Garg4.txt", "w", encoding="UTF-8") as f4:
            for i,j in zip(f,f2):
                c=str(i)+str(j)
                f4.write(c)

#Q5.
import random
A=[]
with open("Ishika_Garg4.txt","a+",encoding="utf8") as f, open("Ishika_Garg4.txt","a+",encoding="utf8") as f4:
    for i in range(1,10):
        A.append(random.randint(1,10))
    for i in A:
        f.writelines(str(i))
    print(A)
    A.sort()
    print(A)
    for k in A:
        f4.write(str(k)+"\n")
