import urllib.request
import json 
import urllib.error
import enum

FN = " (Factory New)"
MW = " (Minimal Wear)"
FT = " (Field-Tested)"
WW = " (Well-Worn)"
BS = " (Battle-Scarred)"

class MarketItem():
  sucess = False
  lowest_price = ""
  median_price = ""
  name = ""
  volume = 0
def GetMarketItem(name):
  strdat = ""
  Item = MarketItem()
  name = name.replace(" ", "+")
  try:
    url = urllib.request.urlopen("http://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=%s" %name)
    data = json.loads(url.read().decode())
    strdat = str(data)
    Item.name = name.replace("+", " ")
  except urllib.error.URLError as e:
    print("ERROR: %s" % e.reason)
    return MarketItem()
  if (strdat.find("success': True") != -1):
    Item.sucess = True
  if (strdat.find('median_price') != -1):
    Item.median_price = data['median_price']
  if (strdat.find('lowest_price') != -1):
    Item.lowest_price = data['lowest_price']
  if (strdat.find('volume') != -1):
    Item.volume = data['volume']
  return Item
def PrintMarketItem(it, volume = False):
  if (len(it.name) > 0):
    print(it.name + ": ")
  if (len(it.median_price) > 0):
    print(it.median_price)
  elif (len(it.lowest_price) > 0):
    print(it.lowest_price)
  else:
    print("No valid price found!")
  if (volume and len(it.volume) > 0):
    print(it.volume)


PrintMarketItem(GetMarketItem("AWP | PAW" + FN), True)
