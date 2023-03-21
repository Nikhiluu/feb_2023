'''
syntax:
for variable in sequence:
    statements
'''
for i in range(1,10):#index starts from one so 1-9 prints
    print(i)

for nikhil in range(1,10,2):#It skips one value
    print("nikhil",nikhil)
for i in "pythonlife":
    print(i,end='')
print()
for i in "pythonlife":
    if i=='l':
        break
    else:
        print(i)
'''
for i in sequence:
    for i in sequence:
        statements(s)
    statements(s)
'''
for i in range(1,5):
    for j in range (i):
        print(i,end='')
    print()
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end="")
    print()
    
'''
While Syntax:

While condition:
       statement(s)
'''


while True:
    print("james bond")
    if True:
        break




a=True
while a:
    print("hii")
    a=False
#----------------------------------------------------------------#
nikhil=0
while nikhil<10:
    print("nikhil",nikhil)
    nikhil+=1
    
i=1
while i<=3:
    print(i,"Outer loop executed once")
    j=1
    while j<=3:
        print(j,"inner loop executed untill condition true")
        j+=1
    i+=1

if True:
     pass




# For Loop is Faster than While Loop
for i in range(11):
    print("for loop",i)

i = 0
while i <= 10:
    print("while loop",i)
    i = i + 1
