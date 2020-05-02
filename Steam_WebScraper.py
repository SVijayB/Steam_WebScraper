import urllib.request
import json
import enum
from data import *
import time
import re
from re import sub

class MarketItem():
    sucess = False
    price = ""
    name = ""
    volume = 0

def GetMarketItem(name):
	strdata = ""
	Item = MarketItem()
	Item.name = name
	temp_name = name.replace(" ", "+")
	
	try:
		url = urllib.request.urlopen("http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=%s" %temp_name)
		data = json.loads(url.read())
		strdata = str(data)
	except:
		print("ERROR: UNABLE TO LOCATE ITEM")
		return MarketItem()
	
	if (strdata.find("success': True") != -1):
	    Item.sucess = True
	    Item.price = data['lowest_price']
	    Item.volume = data['volume']
	return Item

def Result(item):
	if (item.sucess):
		print("\nData Collected : ")
		print(item.name + ": ")
		print("Lowest Price :",item.price)
		print("Volume :" ,item.volume)
	else:
		print("Invalid Item. Please check Item name again.")

Result(GetMarketItem("Nova | Polar Mesh" + WW))

min_price = float(input("Enter the minimum price below which you want to be notified: "))

def main():
	item = MarketItem()
	price = float(sub(r'[^\d.]', '', item.price))
	while(True):
		if (price < min_price):
			print("We found a lesser price !")
			return
		else:
			print('Searching...')
			time.sleep(20)
			GetMarketItem(item.name)

if __name__ == "__main__":
    main() 
	