#Q1.
year=int(input("Enter year="))
if(year%4==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

#Q2.
l=int(input("Enter length="))
b=int(input("Enter breadth="))
if(l==b):
    print("This is a square")
else:
    print("This is a rectangle")

#Q3.
a=int(input("Enter age of 1st person="))
b=int(input("Enter age of 2nd person="))
c=int(input("Enter age of 3rd person="))
if(a>b>c):
    print(a,"is oldest and",c,"is youngest")
elif(a>c>b):
    print(a, "is oldest and",b, "is youngest")
elif(b>c>a):
    print(b, "is oldest and", a, "is youngest")
elif(b>a>c):
    print(b, "is oldest and", c, "is youngest")
elif(c>a>b):
    print(c, "is oldest and", b, "is youngest")
else:
    print(c, "is oldest and", a, "is youngest")

#Q4.
var=int(input("Enter points between 0 and 200="))
if(1<var<50):
    print("Sorry!No prize this time")
elif(51<var<150):
    print("Congratulations!You won a wooden dog")
elif(151<var<180):
    print("Congratulations!You won a book")
elif(181<var<200):
    print("Congratulations!You won chocolates")
else:
    print("Invalid points. Enter number between 1-200")

#Q5.
unn=int(input("Enter number of units that you are purchasing="))
if(0<unn<=10):
    print("Total cost is -",unn*100)
elif(unn>10):
    unnn=(unn-(unn*0.1))*100
    print("Total cost is -",unnn)
else:
    print("Enter positive number")












