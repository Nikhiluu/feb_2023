#forzenset is a immutable version of python set object.
nikhil={1,2,3,4}
print(type(nikhil))
nikhil.add(89)
print(nikhil)
n=frozenset(nikhil)
print(type(n))
#print(n[0]) no index
d=list(n)
d.append(1)
print(d)