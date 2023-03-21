#Read
f=open("demo.txt", mode="r")
content=f.read()
print(content)
f.close()

#Write
f=open("demo.txt",mode="w")
f.write("this is write function")
f.close() #the previous data get lost so we use append

#Append
f=open("demo.txt",mode="a")
f.write(" this is append mode")
f.close()

#readline
f=open("demo.txt",mode="r")
content=f.readline()
print(content)
f.close()

#readlines
f=open("demo.txt",mode="r")
content=f.readlines()
print(content)
f.close()

f=open("demo.txt",mode='r')
cotent=f.readlines()
print(len(content))
f.close()

f=open("demo.txt",mode='r')
content=f.read(10)
print(content)
f.close()

#reading file in 'r+' mode
with open('demo.txt','r+') as fd:
    print(fd.tell())
    print(fd.read())
    print(fd.tell())
    
#reading file in w+ mode
with open("demo.txt","w+") as fd:
    print(fd.tell())
    c=fd.write("this is w+")
    print(fd.read())
    print(fd.tell())
#write file in 'r+' mode
with open("demo.txt",'r+') as fd:
    fd.write("New text")

#write file in 'w+' mode
with open("demo.txt",'w+') as fd:
    fd.write("New text")

#opening file in "w+" mode when it does not exist
with open("nikhil.txt","w+") as fd:
    pass
#opening file in "r+" mode when it does not exist
#with open("nikhil2.txt","r+") as fd:
    pass


#tell
fp=open("demo.txt",'r')
fp.read(8)
print(fp.tell())
fp.close()
fp=open("demo.txt",'r')
print(fp.tell())
fp.close()
print('\n')

#seek
fp=open("demo.txt",'r')
print(fp.tell())
fp.read(2)
print(fp.tell())
fp.seek(0)
print(fp.tell())
fp.close()

#list-writelines-text & text-readlines-list
file=open("demo.txt",mode="r")
content=file.read()
v=str(content)
print(v)
f=v.split()
print(f)
f.insert(0,'Nikhil')
print(file.tell())
file.close()
file=open("demo.txt",mode='w')
print(f)
for i in f:
    file.writelines([i])