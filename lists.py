#lists
msd=[]
raina=list()
print(msd)
print(raina)
msd=[1,2,3,4,5,7]
msd[1]="Nikhil"
print(msd)
print(msd[:])
print(msd[::])
print(msd[0:])
print(msd[2:])
print(msd[:4])
print(msd[-5:])
print(msd[-3:-1])
print(msd[:-1])
print(msd[1:1])
print(msd[0:6:2])
print(msd[0:6:-1])
print(msd[::-1])
#List methods
nikhil=[1,2,3,1,1,1,4,5,6]
print('\n')
#append
nikhil.append('Nikhil')
print(nikhil)
#count
print(nikhil.count(1))
#clear
nikhil.clear()
print(nikhil)
nikhil=[1,2,3,1,1,1,4,5,6]
#copy
n=nikhil.copy()
print(n)
#n.append("nikhil")
print(n)
#extend
nikhil.extend(['Nikhil','MSD','Raina'])
print(nikhil)
#index
print(nikhil.index('MSD'))
#insert
nikhil.insert(1,"Sachin")
print(nikhil)
#pop
nikhil.pop(3)
print(nikhil)
#reverse
nikhil.reverse()
print(nikhil)
#remove
nikhil.remove("Raina")
print(nikhil)
#sort
nikhil=[1,2,3,1,1,1,4,5,6]
nikhil.sort(reverse=True)
print(nikhil)


print('\n')
#print one value indexs
nikhil=[1,2,3,1,1,1,4,5,6]
for i in range(len(nikhil)):
    if nikhil[i]==1:
        print(i)
print('\n')
#replace one by string
nikhil=[1,2,3,1,1,1,4,5,6]
for i in range(len(nikhil)):
    if nikhil[i]==1:
        nikhil[i]="Nikhil"
print(nikhil)
#list comprehension
#odd number or even numbers
print(["Even" if i%2==0 else "odd" for i in range(1,10)])
print([ "even" if i%2==0 else 'odd' for i in range(1,10)])
#square numbers
print([num**2 for num in range(1,10)])
#starting letter of word
print([word[0] for word in ["apple",'banana','carrot']])

#print positve numbers
print([num for num in[-2,-1,0,1,2,3] if num>0])
print()