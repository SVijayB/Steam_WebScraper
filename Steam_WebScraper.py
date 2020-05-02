import requests
from bs4 import BeautifulSoup
import smtplib
import re
import time

headers = {"User Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

def check_price_Steam():
	page = requests.get(URL,headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	price = soup.find("span", class_="market_listing_price market_listing_price_with_fee")
	price = price.text.strip()  
	if(price=="Sold!"):
		time.sleep(5)
		check_price_Steam()
	temp = re.findall(r"[-+]?\d*\.\d+|\d+", price)
	result = 0.0
	result = ".".join(temp).strip()
	result = float(result)
	print("Presently the least value of given Item is :", price.strip())
	return result


URL = input("\nEnter the URL of the product you want to check the price of: ")
current_price = check_price_Steam()
print("Note : Convert given price to your currency and then enter minimum price.")
print("Current value of item in decimals : ",current_price)
min_price = float(input("Enter the minimum price below which you want to be notified: "))

def main():
	a = True
	while(a==True):
		print('Searching...')
		time.sleep(3)
		check_price_Steam()
		if current_price < min_price:
			print("We found your product at a lesser price!")
			print("You will be saving : ", round(min_price - current_price, 2))
			return

if __name__ == "__main__":
    main()