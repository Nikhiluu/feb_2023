#Tuples
t=()
x=tuple()
print(type(x),type(t))
nikh=(1,2,3,44)
print(len(nikh))
print(nikh[1])
print(min(nikh))
print(max(nikh))
print(sum(nikh))
#connact
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)
d=zip(t1,t2)
print(d)

t1=(1,2,3)
t2=(4,5,6)
for i,j in zip(t1,t2):
    print(i+j)

t1=(1,2,3)
t2=(4,5,6)
l=[]
for i,j in zip(t1,t2):
    l.append(i+j)
print(l)
print(tuple(l))