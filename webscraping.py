#Web Scraping
import requests
import pandas as p
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=mi+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mi+mobiles%7CMobiles&requestId=613aebbf-3115-44dd-86c4-610698cd11f0&as-searchtext=mi%20")
soup=BeautifulSoup(response.content,"html.parser")
#print(soup)
names=soup('div',class_="_4rR01T")
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
#print(name)
prices=soup('div',class_="_30jeq3 _1_WHN1")
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
#print(price)
ratings=soup('div',class_="_3LWZlK")
rating=[]
for i in ratings[0:20]:
    d=i.get_text()
    rating.append(d)
#print(rating)
images=soup('img',class_="_396cs4")
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
#print(image)
links=soup.find_all('a',class_="_1fQZEK")
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)
print(link)

df=p.DataFrame()
df["ModelName"]=name
df["MobilePrice"]=price
df["MobileRatings"]=rating
df["MobileImages"]=image
df["MobileLinks"]=link
df.to_csv("Mobiles_data.csv")

