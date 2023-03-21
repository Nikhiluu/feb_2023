#Program to build a table
num=1
for i in range(1,11):
    n= num*i
    print(f"{num}*{n}={n}")
#using list comprehension display cubic values
num=1
for k in range(1,11):
    j=num*k
print(f"{num}*{j}={j}")
print([num**3 for num in range(1,11)])
print("\n")
for i in range(1,5):
    for j in range (i):
        print(i,end="")
    print()
    
print("\n")
for i in range(1,6):
    for j in range(i):
        print("*",end='')
    print()
    
#Print largest number
print("\n")
a,b,c=40,50,30
if a>b and a>c:
    print(a," is the largest number")
elif b>a and b>c:
    print(b," is the largest number")
else:
    print(c," is the largest number")