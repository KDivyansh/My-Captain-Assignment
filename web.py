#WEB SCRAPINGG

import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.newegg.com/global/in-en/p/3D0-000A-00001'

page = requests.get(url)

soup = bs(page.content,'html.parser')

title = soup.find_all('h1', attrs={"class":"product-title"})[0].get_text()

price = soup.find_all('div',attrs={"class":"price-current"})[0].get_text()

#print("\nTitle\n",title,"\nPrice\n",price)

#chkprice = price

np = ""
for i in range(len(price)):
    #removing '₹' , ',' and ' ' from price
    if price[i] != '₹' and price[i] != ' ' and price[i] != ',':   
        np=np+price[i]

#Converting PRICE  to float
np = float(np)

title = title[0:19]

#Checking condition as per MY Wish
if np <= 5000:
    print("It is a buy, Hurry up and buy the\n",title,"as its price is:\n",price)
else:
    print("Wait a little longer as",title,"'s price is:\n",price)

