import requests
from bs4 import BeautifulSoup
import lxml

PRODUCT_URL = "https://www.amazon.in/Atomic-Habits-James-Clear/dp/1847941834/ref=sr_1_2?keywords=atomic+habits&qid=1657868550&s=books&sprefix=atomi%2Cstripbooks%2C443&sr=1-2"

headers = {
    "Accept-Language" : "en-US,en;q=0.5",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
}

response = requests.get(url=PRODUCT_URL, headers=headers).text
# print(response)
soup = BeautifulSoup(response, "lxml")
item_price_text = soup.find(name="span",class_="header-price").get_text()
item_price = float(item_price_text.split("₹")[1])
# print(item_price)

if (item_price < 300):
    # send email
    # or text
    # but here i'll just print to console
    print(f"Item Price Dropped to {item_price}. You can buy it now.")