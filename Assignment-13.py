#Q1.
print("Exception is - ZeroDivisionError")
a=3
try:
    if(a<4):
        a=a/(a-3)
except ZeroDivisionError:
    print("Zero division error")
else:
    print(a)

#Q2.
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("Element at 3rd index is not present")

#Q3.
print("An exception")

#Q4.
print("-5.0")
print("a/b result in 0")

#Q5.
try:
    import Ishika_Garg
    a=int(input("Enter any number="))
    A=[]
    for i in range(a):
        b=int(input("Enter number="))
        A.append(b)
    c=int(input("Enter position that you want"))
    print(A[c])
except ImportError:
    print("No such file exists")
except ValueError:
    print("Please enter integer")
except IndexError:
    print("Element at %d index is not present"%c)

#Q6.
class AgeTooSmallError(Exception):
    pass
def show1():
    try:
        a = int(input("Enter age="))
        if (a < 18):
            raise AgeTooSmallError
    except AgeTooSmallError:
        print("You are under 18")
        show1()
    except ValueError:
        print("Please enter integer")
    else:
        print("Your age is appropriate")
show1()

#Q6..
class AgeTooSmallError(Exception):
    pass
a=0
while (a < 18):
    try:
        a = int(input("Enter age="))
        if (a < 18):
            raise AgeTooSmallError
    except AgeTooSmallError:
        print("You are under 18")
    except ValueError:
        print("Please enter integer")
    else:
        print("Your age is appropriate")





