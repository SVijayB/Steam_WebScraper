import urllib.request
import json
import enum
from data import *

class MarketItem():
    sucess = False
    lowest_price = ""
    name = ""
    volume = 0

def GetMarketItem(name):
	strdata = ""
	Item = MarketItem()
	Item.name = name
	temp_name = name.replace(" ", "+")
	
	try:
		url = urllib.request.urlopen("http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=%s" %temp_name)
		print("\nURL for reference: http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=%s" %temp_name)
		data = json.loads(url.read())
		strdata = str(data)
	except:
		print("ERROR: UNABLE TO LOCATE ITEM")
		return MarketItem()
	
	if (strdata.find("success': True") != -1):
	    Item.sucess = True
	    Item.lowest_price = data['lowest_price']
	    Item.volume = data['volume']
	return Item

def Result(item):
	if (item.sucess):
		print("\nData Collected : ")
		print(item.name + ": ")
		print("Lowest Price :",item.lowest_price)
		print("Volume :" ,item.volume)
	else:
		print("Invalid Item. Please check Item name again.")

Result(GetMarketItem("Nova | Polar Mesh" + WW))