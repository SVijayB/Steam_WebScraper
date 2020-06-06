from re import *
import enum
import urllib.request
import json
import time
import sys
from Modules.Mailing import *
from Modules.Currency import *

class MarketItem():
	def __init__(self):
		self.success=False
		self.price = ""
		self.name = ""
		self.volume = 0
		self.symbol = ""

	def give_success(self, success):
		self.success = success

	def give_name(self, name):
		self.name = name
	
	def give_price(self, price):
		self.price = price
	
	def give_volume(self, volume):
		self.volume = volume

	def give_symbol(self, symbol):
		self.symbol = symbol

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
		print("\nERROR: UNABLE TO LOCATE ITEM")
		return MarketItem()
	
	if (strdata.find("success': True") != -1):
	    Item.give_success(True)
	    Item.give_price(data['lowest_price'])
	    Item.give_volume(data['volume'])

	return Item

def Result(item):
	if (item.success):
		lowest_price = currency(item.price)
		item.price = float(sub(r'[^\d.]', '', lowest_price))
		item.symbol = lowest_price.replace(str(item.price),"")

		print("\nData Collected : ")
		print("\t"+item.name)
		print("\tLowest Price :", lowest_price)
		print("\tVolume :" ,item.volume)
		return item
	else:
		print("Invalid Item. Please check Item name again.")
		return item


def main(item):
	if (item.success):
		print("\nEnter the minimum price below which you want to be notified")
		min_price = None
		var = None
		while (isinstance(min_price,float)) is not True:
			try:
				min_price = float(input("> "))
				if(isinstance(min_price,float)) is not True:
					raise ValueError
			except ValueError:
				print("ERROR : INVALID TYPE. ENTER ONLY NUMBERS")
		price = item.price
		
		print(("Would you like to be notified via mail?(Yes/No)"))
		mail = ""
		while (mail!="Yes" and mail!="yes" and mail!="y" and mail!="No" and mail!="no" and mail!="n"):
			try:
				mail = (input("> "))
				if(mail!="Yes" and mail!="yes" and mail!="y" and mail!="No" and mail!="no" and mail!="n"):
					raise ValueError
			except ValueError:
				print("ERROR : INVALID CHOICE")
		if(mail=="Yes" or mail=="yes" or mail=="y"):
			print("\nMake sure you enable less secure app access.\nTo do this, go to",
					"Google Account settings and enable Less secure app access.")
			username = str(input("Enter your GMAIL User name\n> "))
			password = str(input("Enter your GMAIL Password\n> "))
		else:
			print("\nOkay, You won't be receiving an E-mail!")

		while(True):
			if (price < min_price):
				print("\nWe found an Item at a lesser price !")
				print("You are saving", abs(price-min_price), item.symbol)
				if(mail=="Yes" or mail=="yes" or mail=="y"):
					try:
						email(username,password)
					except:
						print("ERROR : WRONG E-MAIL CREDENTIALS")
						print("Unable to send E-mail")
				print("\nThanks for Using Steam_WebScraper")
				input("Press any key to exit ")
				sys.exit(0)
			else:
				print('Searching...')
				time.sleep(4)
				GetMarketItem(item.name)
	else:
		input("Press any key to exit ")