import urllib.request
import json
import enum
from data import *
import time
from re import *
import smtplib
import sys

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
		print("\nERROR: UNABLE TO LOCATE ITEM")
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
	if (item.success):
		min_price = float(input("Enter the minimum price below which you want to be notified: "))
		price = float(sub(r'[^\d.]', '', item.price))
		
		mail = input(("Would you like to be notified via mail?(Yes/No) : "))
		if(mail=="Yes" or mail=="yes" or mail=="y"):
			print("\nMake sure you enable less secure app access. To do this, go to",
					"Google Account settings and enable Less secure app access.")
			username = str(input("Enter your GMAIL User name : "))
			password = str(input("Enter your GMAIL Password : "))
		else:
			print("Okay, You won't be receiving an email!")

		while(True):
			if (price < min_price):
				print("We found a lesser price !")
				print("You are saving :",round(min_price - price, 2),"!")
				if(mail=="Yes" or mail=="yes" or mail=="y"):
					email(item,username,password)
				sys.exit(0)
			else:
				print('Searching...')
				time.sleep(4)
				GetMarketItem(item.name)
	else:
		print("Exiting Program.")

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

def email(item,username,password):
	host = "smtp.gmail.com"
	port = 587
	message = "Hey! We found your Steam Item at a lower price!"
	connection = smtplib.SMTP(host,port)
	connection.ehlo()
	connection.starttls() 
	connection.login(username,password)
	connection.sendmail(username,username,message)
	connection.quit()

if __name__ == "__main__":
	main(Result(GetMarketItem(name())))
	input()
	