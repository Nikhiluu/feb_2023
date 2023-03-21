#Strings
nikhil="pythom"
msd='python'
raina='''python'''
print(type(nikhil),type(msd),type(raina))
nikhil="python's"
print(nikhil)
#Methods
nikhil="This is My book"
#upper
print(nikhil.upper())
#lower
print(nikhil.lower())
#title
print(nikhil.title())
print('\n')
msd="         What a shot      "
#lstrip
print(len(msd))
print(msd.lstrip())
print(len(msd))
#rstrip
print(msd.rstrip())
print(len(msd))
#strip
msd="         What a shot      "
print(len(msd))
print(msd.strip())
print(len(msd))
#count
raina="this is my pen"
print(raina.count(" is"))
#starts with
print(raina.startswith("Th"))
print(raina.startswith("This"))
print(raina.startswith("is"))
#ends with
print(raina.endswith("book"))
print(raina.endswith("k"))
print(raina.endswith("is"))
#find
print(raina.find("is"))
print(raina.find("my"))
#index
print(raina.index("is"))
print(raina.index("my"))
#isalpha
nikhil="My name is"
print(nikhil.isalpha())
#isnumeric
n="1234"
print(n.isnumeric())
#isalnum
x="12hf4f"
print(x.isalnum())
#format
print("My name is {}".format("Nikhil"))
print("My name is {} and i am learning {}".format("nikhil","python"))
#join
msd="this is my book"
dhoni="and this is my pen"
c=msd.split()
d=dhoni.split()
print(c,d)
e=c+d
f=" ".join(e)
print(f)
d="this is my book"
print(d.find("that"))
print(d.count("is"))
print([num**3 for num in range (1,5)])
n="this is string class"
m=n.replace("is","are")
print(m)
x="this is string class"
a=x.split()
n=[]
for i in a:
    if i=="is":
        i="are" 
        n.append(i)
    else:
        n.append(i)
f=" ".join(n)
print(f)
#tasks
about="Hi my name is Nikhil. This is my Books and i am writing about the strings. This topic is very simple."
x=about.split()
d=[]
print(about.replace(" is"," are").replace(" This"," That"))