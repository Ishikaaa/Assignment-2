#Q1.
class Animal():
    def animal_attribute(self):
        print("Animal Attribute calling")
class Tiger(Animal):
    def show1(self):
        self.animal_attribute()
T=Tiger()
T.show1()

#Q2.
print("a.f(),b.f() -- AB")
print("a.f(),b.f() -- AB")

#Q3.
class Cop():
    def __init__(self):
        self.name=input("Enter name=")
        self.age=int(input("Enter age="))
        self.we=input("Enter work experience=")
        self.d=input("Enter designation=")
    def display(self):
        print("Name=%s\tAge=%d\tWork experience=%s\tdesignation=%s"%(self.name,self.age,self.we,self.d))
    def update(self):
        self.name = input("Enter update name=")
        self.age = int(input("Enter update age="))
        self.we = input("Enter update work experience=")
        self.d = input("Enter update designation=")
class Mission(Cop):
    def add_mission_details(self):
        self.md=input("Enter details of mission of %s ="%(self.name))
    def mission_display(self):
        print("Name=%s\tAge=%d\tWork experience=%s\tdesignation=%s\tMission=%s" % (self.name, self.age, self.we, self.d,self.md))
M=Mission()
M.display()
M.update()
M.display()
M.add_mission_details()
M.mission_display()

#Q4.
class shape():
    l = int(input("Enter length="))
    b = int(input("Enter breadth="))
    def show1(self):
        return self.l
    def show2(self):
        return self.b
class rectangle(shape):
    def show3(self):
        self.show1()
        self.show2()
        self.A=self.l*self.b
    def show4(self):
        print("Area of rectangle =",self.A)
class square(shape):
    def show3(self):
        self.A=self.l*self.l
    def show4(self):
        print("Area of square =",self.A)
S=shape()
a=S.show1()
b=S.show2()
if(a!=b):
    R=rectangle()
    R.show3()
    R.show4()
else:
    S=square()
    S.show3()
    S.show4()
