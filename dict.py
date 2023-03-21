nikhil={}
nik=dict()
print(type(nikhil),type(nik))
nikhil={1:"Nikhil",2:"Raju","ravi":3,(1,2):6}
print(nikhil)
print(nikhil[1])
print(nikhil["ravi"])
#Methods
#clear
print('\n')
print(nikhil)
nikhil.clear()
print(nikhil)
nikhil={1:"Nikhil",2:"Raju","ravi":3,(1,2):6}
#copy
x=nikhil.copy()
print("x=",x)
#get
print(nikhil.get(0))
print(nikhil.get(1))
#items
print(nikhil.items())
#keys
print(nikhil.keys())
#values
print(nikhil.values())
#pop
print(nikhil.pop(1))
#update
nikhil.update({3:"Msd"})
print(nikhil)
#Nested Dict
d={
    "a":1,
    2:"Msd",
    'c':{1:"Nikhil"}
}
print(d["c"][1])

a={
    1:7,
    2:3,
    "c":{(1,2):"msd"}
}
print(a['c'][(1,2)])
print("\n")
print("Nested Dictionary")
x={
    1:'name',
    2:9,
    3:"sachin",
    'cri':{7:"msd",10:"sachin"}
}
print(x["cri"][10])
print(x.get("cri").get(10))

for i in {1:"name",2:"is",3:"nikhil"}.items():
    print(i)
for i,j in {1:"name",2:"is",3:"nikhil"}.items():
    print(i,j)
m_user={"Nikhil":7,"Msd":7}
user_name ="Nikhil"
if user_name in m_user:
    print("Yes")
else:
    print("No")
    
