'''                 object oriented programming                        '''

'''
class
object
self
__init__
'''

# class(template)
'''
1.we will define class by using 'class' keyword
2.blue print to create a objects
3.collection of objects is called class
'''
#ex fruits

# object
# physical entity(real)
'''
1.an instance of a class
2.memory is created when it declared
'''
#ex apple,orange,mango

# class Pramod():# class defination
#     # constructors
#     # functions
#     # variables
# attribute (variable) data members
'''
age=20 
color='blue'
'''
# method(behaviour) or functions , member functions
'''
eat() 
sleep()
'''

# self keyword
'''
we can access the attributes and methods of the class(current class only)
'''
class Nikhil():#class define
    def fun(self):
        print("Hello How Are You!")
# # object name=Class name
obj=Nikhil()
#obj.method()
obj.fun()


class Msd:
    def raina(self):
        print("My captain is MSD")
obj1=Msd()
obj1.raina()


class Ex1:
    a=10
    def n(self):
        print("this is class")
obj=Ex1()
print(obj.a)
obj.n()

class Nikhil():
    a=20
    def show(self):
        print("this is class")
obj1=Nikhil()
obj2=Nikhil()
print(obj1.a)
print(obj2.a)

print("\n")
class Nik():
    a=30
    def Display(self):
        print(self.a)
ram=Nik()
shaym=Nik()
ram.Display()
shaym.Display()

# # # __init__

# # '''
# # Constructors are generally used for instantiating an object. 
# # The task of constructors is to initialize(assign values)
# # to the data members of the class when an object of the class 
# # is created.
# # In Python the __init__() method is called the constructor
# # and is always called when an object is created

# # does'nt support multiple constructor
# # '''

a=100
def fun1():
    a=10
fun1()
def fun2():
    d=a
fun2()

class Nikhil():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def Test(self):
        print(self.a,self.b,self.c)
obj=Nikhil(1,2,3)
obj.Test()

print("\n")

class Bike():
    def __init__(self,Bike_Name,CC,Color,Price,Mileage):
            self.h=Bike_Name
            self.i=CC
            self.j=Color
            self.k=Price
            self.l=Mileage
    def Bike_Details(self):
        print("Bike Name:",self.h)
        print("Bike CC:",self.i)
        print("Bike Color:", self.j)
        print("Bike Price:", self.k)
        print("Bike Mileage:", self.l)
bn="Honda"
bcc=1000
bc="Black"
bp=100000
bm=60
bikeobj=Bike(bn,bcc,bc,bp,bm)
bikeobj.Bike_Details()

class Nikhil:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(a)
    def Output(self):
        print(self.a,self.b,self.c)
obj=Nikhil(1,2,3)
obj.Output()



class Mobile:
    def __init__(self,name,color,ram,storage,camera,price):
        self.name=name
        self.color=color
        self.ram=ram
        self.storage=storage
        self.camera=camera
        self.price=price
    def Mobile_Details(self):
        print("Mobile Name:",self.name)
        print("Mobile Color:",self.color)
        print("Mobile Ram:",self.ram)
        print("Mobile Storage:",self.storage)
        print("Mobile Camera:",self.camera)
        print("Mobile Price:",self.price)
mn="lava"
mco="white"
mr="4gb"
ms="32gb"
mc="48MP"
mp=4000
mobile=Mobile(mn,mco,mr,ms,mc,mp)
mobile.Mobile_Details()
    
class Mobile:
    def __init__(self,name,color,ram,storage,camera,price):
        self.name=name
        self.color=color
        self.ram=ram
        self.storage=storage
        self.camera=camera
        self.price=price
    def Mobile_Details(self):
        print("Mobile Name:",self.name)
        print("Mobile Color:",self.color)
        print("Mobile Ram:",self.ram)
        print("Mobile Storage:",self.storage)
        print("Mobile Camera:",self.camera)
        print("Mobile Price:",self.price)
while True:
    mn=input("Enter the Mobile name: ")
    mco=input("Enter the Mobile Color: ")
    mr=input("Enter the Mobile Ram: ")
    ms=input("Enter the Mobile Storage: ")
    mc=input("Enter the Mobile Camera: ")
    mp=input("Enter the Mobile price: ")
    mobile=Mobile(mn,mco,mr,ms,mc,mp)
    mobile.Mobile_Details()