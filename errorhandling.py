try:
    print(a)
except:
    print("error undhi")
else:
    print("error ledhu")
finally:
    print("always")
    
print("\n")
try:
    print('Hello world')
except:
    print("error undhi")
else:
    print("error ledhu")
finally:
    print("always")
print("\n")
#to know the type of error
try:
    print(1+"nikhil")
except Exception as k:
    print(k)  
print("\n")
#knowing error
try:
    print(a)
except NameError:
    print("Name Error")
except ZeroDivisionError:
    print("Divison Error")
except SyntaxError:
    print("Syntax Error")
print('\n')
try:
    print(1/0)
    print(a)
except NameError:
    print("Name Error")
except ZeroDivisionError:
    print("Divison Error")
except SyntaxError:
    print("Syntax Error")
print("\n")

try:
    print(1/0)
    print(a)
except ValueError:
    print("Name Error")
except ZeroDivisionError:
    print("Divison Error")
except SyntaxError:
    print("Syntax Error")
finally:
    print("Name Error")
    