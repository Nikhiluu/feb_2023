#Lambda
x=lambda a,b,c:a+b+c
print(x(1,2,3))
l1=[12,4,8,7,10]
l2=[]
for i in l1:
    t= lambda a:a+1
    l2.append(t(i))
print(l2)
f=lambda a: a*3
print(f)
print('\n')
#Filter
age=[12,34,56,14,17,23]
def myFun(x):
    if x>18:
        return True
    else:
        return False
adults=filter(myFun,age)
print(list(adults))
print('\n')
#Map
def caladd(n):
    return n+n
numbers=(1,2,3,4)
result=map(caladd,numbers)
print(list(result))
print("\n")
#Reduce
from functools import reduce
d=reduce(lambda a,b:a+b,[2,3,4,5])
print(d)
print("\n")
#Generator
def genfun():
    yield 1
    yield 2
    yield 3
x=genfun()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print("\n")
#retun
def fun():
    return 1+3
    return 4+5
print(fun())
print(fun())
print("\n")
#Nested Function
def outer():
    print("Outer")
    def inner():
        print("inner")
    inner()
outer()

g=[2,343,5,78,98,100]
great=[]
def greater(x):
    if x>2:
        great.append(x)
for i in g:
    greater(i)
print(great)


def greater(x):
    if x>2:return True
print(list(filter(lambda x:x>2,[2,325,23,546,363,6])))
