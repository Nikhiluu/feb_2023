nikhil={}
print(type(nikhil))#By default it takes as dict
ni={1,2,3,3}
print(type(ni))#when we specify elements it take as set
letters="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
print("strings: ",str(letters))
print("lists: ",list(letters))
#print("Dict: ",dict(letters))
print("Set: ",set(letters))
nikhil={1,2,3,4,5,3,3}
print(nikhil)
nikhil.add(89)
print(nikhil)
nikhil.clear()
print(nikhil)
n={1,2,3,4,6,0}
n.pop()#delete smallest element
print(n)
n.remove(6)#delete specified element
print(n)
n.update({1,2,3,4,5,6,78})
print(n)

print("\n")
#set operations
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
s3={1,2,3}
s4={4,5,6}
print(s3.isdisjoint(s4))
s5={1,2,3,4}
s6={1,2,3,4,5,6}
print(s5.issubset(s6))
print(s6.issuperset(s5))
print(s1.union(s2,s3,s4,s5,s6))