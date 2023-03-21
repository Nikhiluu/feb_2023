from datetime import datetime
name=input("Enter your name: ")
#List of items
lists='''
Rice    Rs  20/kg
Sugar   Rs  30/kg
Salt    Rs  20/kg
Oil     Rs  80/lit
Paneer  Rs  110/kg
Maggi   Rs  50/kg
Boost   Rs  90/each
Colgate Rs  85/each
'''
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={
    "rice":20,
    "sugar":30,
    "Oil":80,"panner":110,"Maggi":50,"Boost":90,"Colgate":85}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exist:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter the quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item not available")
    else:
        print("You entered wrong number")
    inp=input("Can i bill the items Yes or No:")
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*"=","Nikhil Super Market",25*"=")
            print(28*" ","Yerraguntla")
            print("Name:",name,30*" ","Date: ",datetime.now())
            print(75*"-")
            print("sno",8*" ","items",8*" ","Quantity",3*" ","Price")
            for i in range(len(pricelist)):
                print(i,8*" ",8*" ",ilist[i],3*" ",qlist[i],plist[i])
                print(75*"-")
                print(50*" ","TotalAmount:","RS",totalprice)
                print("gst amount",50*" ","Rs",gst)
                print(75*"-")
                print(50*" ","finallAmount:","RS",finalamount)
                print(75*"-")
                print(50*" ","Thanks for visting")
                print(75*"-")