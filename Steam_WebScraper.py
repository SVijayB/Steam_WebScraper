import urllib.request
import json
import enum
from data import *
import time
import re
from re import sub

class MarketItem():
	def __init__(self):
		self.success=False
		self.price = ""
		self.name = ""
		self.volume = 0

	def give_success(self, success):
		self.success = success

	def give_name(self, name):
		self.name = name
	
	def give_price(self, price):
		self.price = price
	
	def give_volume(self, volume):
		self.volume = volume

def GetMarketItem(name):
	strdata = ""
	Item = MarketItem()
	Item.give_name(name)
	temp_name = name.replace(" ", "+")
	
	try:
		url = urllib.request.urlopen("http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=%s" %temp_name)
		data = json.loads(url.read())
		strdata = str(data)
	except:
		print("ERROR: UNABLE TO LOCATE ITEM")
		return MarketItem()
	
	if (strdata.find("success': True") != -1):
	    Item.give_success(True)
	    Item.give_price(data['lowest_price'])
	    Item.give_volume(data['volume'])

	return Item

def Result(item):
	if (item.success):
		print("\nData Collected : ")
		print(item.name + ": ")
		print("Lowest Price :",item.price)
		print("Volume :" ,item.volume)
		return item
	else:
		print("Invalid Item. Please check Item name again.")
		return item


def main(item):
	min_price = float(input("Enter the minimum price below which you want to be notified: "))
	price = float(sub(r'[^\d.]', '', item.price))
	while(True):
		if (price < min_price):
			print("We found a lesser price !")
			print("You are saving :",round(min_price - price, 2),"!")
			return
		else:
			print('Searching...')
			time.sleep(4)
			GetMarketItem(item.name)

def name():
	for x in range(len(csitems)): 
		print (x+1,csitems[x])
	wep = input("Pick the number that matches the Item you are looking for : ")
	wep = int(wep)-1
	print("Selected Item :",csitems[wep])
	for x in range(len(quality)): 
		print (x+1,quality[x])
	qual = input("Pick the Quality of skin you are looking for : ")
	qual = int(qual)-1
	print("Selected Quality :",quality[qual])
	nm = input("Enter the name of the skin you are looking for(Has to match steam DataBase) : ")
	final = csitems[wep]+" | "+nm+qualfinal[qual]
	return final

if __name__ == "__main__":
	main(Result(GetMarketItem(name())))
	