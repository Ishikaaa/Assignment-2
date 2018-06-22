# #Q1.
# class Circle():
#     def __init__(self):
#         r=int(input("Enter radius="))
#         self.r=r
#     def getArea(self):
#         A=3.14*self.r*self.r
#         print("Area of a circle",A)
#     def getCircumference(self):
#         C=2*3.14*self.r
#         print("Circumference of a circle=",C)
# c=Circle()
# c.getArea()
# c.getCircumference()

# #Q2.
# class Student():
#     def __init__(self):
#         a=input("Enter name=")
#         b=int(input("Enter roll number="))
#         self.a=a
#         self.b=b
#     def display(self):
#         print("Roll No.-%d\tName-%s"%(self.b,self.a))
# s=Student()
# s.display()

# #Q3.
# class Temperature():
#     def convertFahrenheit(self,b):
#         self.b=b
#         F=((9/5)*self.b)+32
#         print("temperature in Fahrenheit=",F)
#     def convertCelsius(self,b):
#         self.b=b
#         C=(self.b-32)*(5/9)
#         print("Temperature in Celsius=",C)
# t=Temperature()
# a=int(input("Enter 1 to convert Celsius into Fahrenheit and 2 to convert Fahrenheit into Celsius ="))
# if(a==1):
#     b=float(input("Enter temperature in celsius="))
#     t.convertFahrenheit(b)
# elif(a==2):
#     b = float(input("Enter temperature in Fahrenheit="))
#     t.convertCelsius(b)
# else:
#     print("Enter number from 1 or 2")

# #Q4.
# class Moviedetails():
#     def __init__(self):
#         name=input("Enter movie name=")
#         an=input("Enter name of artist=")
#         year=int(input("Enter year fo release="))
#         rat=int(input("Enter ratings of movie="))
#         self.name=name
#         self.an=an
#         self.year=year
#         self.rat=rat
#     def display(self):
#         print("Name of movie=%s\nName of artist=%s\nYear of release=%d\nRatings of movie=%d"%(self.name,self.an,self.year,self.rat))
#     def update(self,n,a,y,r):
#         self.name2= n
#         self.an2= a
#         self.year2= y
#         self.rat2= r
#         print("Name of movie=%s\nName of artist=%s\nYear of release=%d\nRatings of movie=%d"%(self.name2,self.an2,self.year2,self.rat2))
# M=Moviedetails()
# M.display()
# name1=input("Enter updated movie name=")
# an1=input("Enter name of artist of updated movie=")
# year1=int(input("Enter year fo release of updated movie="))
# rat1=int(input("Enter ratings of updated movie="))
# M.update(name1,an1,year1,rat1)

#Q5.
class Expenditure():
    def __init__(self):
        b = int(input("Enter your savings="))
        a=int(input("Enter amount of money you spent="))
        self.a=a
        self.b=b
    def display(self):
        print("Your savings are Rs%d and spent Rs%d"%(self.a,self.b))
    def salary(self):
        self.c=self.a+self.b
    def displaysakary(self):
        print("Total salary=",self.c)
e=Expenditure()
e.display()
e.salary()
e.displaysakary()


