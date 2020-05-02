import urllib.request
import json
import urllib.error
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
    name = name.replace(" ", "+")
    try:
        url = urllib.request.urlopen("http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=%s" %name)
        print("\nURL for reference: http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=%s" %name)
        data = json.loads(url.read().decode())
        strdata = str(data)
        Item.name = name.replace("+", " ")
    except urllib.error.URLError as e:
        print("ERROR: %s" % e.reason)
        return MarketItem()
    if (strdata.find("success': True") != -1):
        Item.sucess = True
    else:
        return MarketItem()
    if (strdata.find('lowest_price') != -1):
        Item.lowest_price = data['lowest_price']
    if (strdata.find('volume') != -1):
        Item.volume = data['volume']
    return Item

def PrintMarketItem(item):
    print("\nData Collected : ")
    if (len(item.name) > 0):
        print(item.name + ": ")
    if (len(item.lowest_price) > 0):
        print("Lowest Price :",item.lowest_price)
    else:
        print("Item Missing, Check Item Name!")
    if (int(item.volume) > 0):
        print("Volume :" ,item.volume)
    else:
        print("Invalid Item. Please check Item name again.")

PrintMarketItem(GetMarketItem("Nova | Polar Mesh" + WW))
