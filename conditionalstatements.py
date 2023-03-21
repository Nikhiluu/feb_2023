#if
if True:
    print("I am if")
#if else
if False:
    print("I am if")
else:
    print("I am else")
#if elif
if False:
    print("I am if")
elif True:
    print("I am elif")
#Examples
#1
a,b=10,20
if a<b:
    print("Yes")
elif a>b:
    print("Yes elif")
else:
    print("Else")
#2
a,b=10,20
if a>b:
    print("Yes")
elif a<b:
    print("Yes elif")
else:
    print("Else")
#3
a=b=10
if a<b:
    print("Yes")
elif a>b:
    print("Yes elif")
else:
    print("Else")
#4
age=20
if age>=18:
    print("You can drive")
else:
    print("You can't drive")
#5
x=int(input("Enter a number:"))
if x>0:
    print("Positive")
elif x<0:
    print("Negative")
else:
    print("Neutral")
    
#Nested if
#Type-1
if True:
    print("This is outer if")
    if True:
        print("This is inner if")
    else:
        print("This is inner else")
else:
    print("This is outer else")
#Type-2
if True:
    print("This is outer if")
    if False:
        print("This is inner if")
    else:
        print("This is inner else")
else:
    print("This is outer else")
#Type-3
if False:
    print("This is outer if")
    if True:
        print("This is inner if")
    else:
        print("This is inner else")
else:
    print("This is outer else")
    
    
#Short hand if(if condition statements)
a=1
b=2
if a<b:print(a)
#short hand if else(satements if condition else statements)
#if condition true return LHS otherwise returns RHS
print(a) if a>b else print(b)

#example
print("\n")
username="nikhil"
password="123"
user=input("Please Enter your username:")
pasw=input("Please Enter your password:")
if user==username and pasw==password:
    print("Login Sucess!")
else:
    print("Login Unsucess")