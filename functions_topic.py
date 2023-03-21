
#function define
def fun_name():
    #function body    
    print("Hello Nikhil")#function is prints when its called
fun_name()#function call
print("\n")
#using for within function
for i in range(3):
    fun_name()
print("\n")
def nikhil():
    print("Hi")
nikhil()
print("\n")
#Prameters inside a function
def msd(a):
    print("That is a",a)
msd("Helicopter shot")
print("\n")
def virat(a):
    print("Virat reached "+str(a)+"runs in Iterantional")
virat(25000)
print("\n")
#add using function and multiple parameters with multiple arguments
def add(a,b):
    print(f"{a}+{b}={a+b}")
add(1,2)
add(13,17)
add(15,25)
print("\n")
#Passing Multiple arugemts in single parameters
def nikhil(a):
    print(a)
nikhil(1200)
def vallepu(*a):#orbitary arguments are used to pass a group of values inside a    
    print(a)
vallepu(1,2,3,4,5)
def raina(**a):#keyword arguments are display the data in dict    
    print(a)
raina(a=1,b=10,c=20,d=30)

