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
	price = price.text  
	result = re.findall(r"[-+]?\d*\.\d+|\d+", price)
	result = float(result[0])
	print("Currently the least value of given Item is : ", result)
	return result


URL = input("Enter the URL of the product you want to check the price of: ")
current_price = check_price_Steam()
min_price = float(input("Enter the minimum price below which you want to be notified: "))

def main():
	a = True
	while(a==True):
		if current_price < min_price:
			print("We found a lesser price !")
			return
		else:
			print('Searching...')
			time.sleep(20)

if __name__ == "__main__":
    main()