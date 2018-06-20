#Q1.
def area():
    r=int(input("Enter radius="))
    A=3.14*r*r
    print("Area of circle =",A)
area()

# Q2.
def perfect(i):
    Sum=0
    for j in range(1,i):
        if(i%j==0):
            Sum=Sum+j
    if(Sum==i):
        print(i)
print("List of perfect numbers from 1 to 1000-")
for i in range(1,1001):
    perfect(i)

#Q3.
def multt(i):
    n=12
    if(i==11):
        return
    else:
        print(n,"*",i,"=",n*i)
        multt(i+1)
i=1
multt(i)

#Q4.
def poww(a,b):
    if(b==0):
        return 1
    else:
        return(a*poww(a,b-1))
a=int(input("Enter number="))
b=int(input("Enter power="))
P=poww(a,b)
print(P)

#Q5.
A={}
def factt(i):
    if(i==1):
        return 1
    else:
        return(i*factt(i-1))
for i in range(5):
    a = int(input("Enter number="))
    FF=factt(a)
    A[a]=FF
print("Dictionary -", A)
