# # inheritance
# # single (parent child)
print("Single inheritance")
class Parent:
    def Output(self):
        print("This is parent class")
class Child(Parent):
    def ChildOutput(self):
        print("This is child class")
i=Child()
i.Output()
i.ChildOutput()

print("\n")
print("Multiple in heritance")
# # multiple(two are more base classes)
class Father:
    def Fo(self):
        print("This is father class")
class Mother:
    def Mo(self):
        print("This is mother class")
class Child(Father,Mother):
    def child(self):
        print("This is child class")
j=Child()
j.child()
j.Fo()
j.Mo()


# # # multilevel(tree)
print("\n")
print("Multi level inheritance")
class Gfather:
    def gf(self):
        print("This is grand father class")
class father(Gfather):
    def f(self):
        print("This is father class")
class child(father):
    def child(self):
        print("This is child class")
k=child()
k.gf()
k.f()
k.child()
# # # # hierarchical(one base with sibiling childs)
print("\n")
print("Hierarchucal inheritance")

class father:
    def f(self):
        print("This is father class")
class Child1(father):
    def child1(self):
        print("This is child1 class")
class Child2(father):
    def child2(self):
        print("This is child2 class")
ice=Child1()
cream=Child2()
ice.f()
ice.child1()
cream.f()
cream.child2()

print("\n")

# Polymorphism
# poly-many
# morph = forms
# 1.method overloading 
# 2.method overridding
print("Polymorphism")
def test(a,b):
    print(a+b)
test(1,1)
test("k","k")
test([1,2],[3,4])
print('\n')
print("Method Overloading")
class MethodOverload:
    def something(self,a,b,c):
        print(a,b,c)
obj=MethodOverload()
obj.something(1,2,3) 
#obj.something(1,2)
class MethodOverload:
    def something(self,a=None,b=None,c=None):
        print(a,b,c)
obj=MethodOverload()
obj.something(1,2,3) 
obj.something(1,2)
obj.something(1)
obj.something()

print('\n')
print("Method Overiding")
class MethodOver:
    def display(self):
        print("This is parent class")
class child(MethodOver):
    def display(self):
        print("This is child class")
obj=child()
obj.display()
print('\n')
class MethodOver:
    def display(self):
        print("This is parent class")
class child(MethodOver):
    def display(self):
        print("This is child class")
        super().display()
obj=child()
obj.display()

#encapsulation

# binding of class (methods and variables(attributes))
# # public 
# # and 
# # private __
# # protected _

class GFather:
    def __init__(self,a):
        self._y=a
        print(self._y)#default calling because we using __init__
class Father(GFather):
    def display1(self):
        print(self._y)
class Child2(Father):
    def display2(self):
        print("child2",self._y)
obj=Child2(12)
obj.display1()
obj.display2()


# #abstraction
#abstract method there is no body
#abstract base class can not  create object
#a class contain one or more abstract methods then it said to be a abc

# Python program demonstrate  
# abstract base class work  
from abc import ABC, abstractmethod
class Mobile(ABC):
    @abstractmethod
    def MobilePrice(self):
        pass
class Mi(Mobile):
    def MobilePrice(self):
        print("Mi Price=10000")
class Realme(Mobile):
    def MobilePrice(self):
        print("Realme Price=15000")
class Oneplus(Mobile):
    def MobilePrice(self):
        print("Oneplus Price=18000")
m=Mi()
m.MobilePrice()
r=Realme()
r.MobilePrice()
o=Oneplus()
o.MobilePrice()
    
        