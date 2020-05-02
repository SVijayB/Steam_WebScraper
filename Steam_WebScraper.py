import urllib.request
import json
import urllib.error
import enum
from data import *

class MarketItem:
    sucess = False
    lowest_price = ''
    name = ''
    volume = 0

def GetMarketItem(name):
    strdata = ''
    Item = MarketItem()
    name = name.replace(' ', '+')
    try:
        url = urllib.request.urlopen("http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=%s" % name)
        data = json.loads(url.read().decode())
        strdata = str(data)
        Item.name = name.replace('+', ' ')
    except urllib.error.URLError as e:
        print ('ERROR: %s' % e.reason)
        return MarketItem()
    if strdata.find("success': True") != -1:
        Item.sucess = True
    if strdata.find('lowest_price') != -1:
        Item.lowest_price = data['lowest_price']
    if strdata.find('volume') != -1:
        Item.volume = data['volume']
    return Item


def PrintMarketItem(it, volume=False):
    if len(it.name) > 0:
        print (it.name + ': ')
    if len(it.lowest_price) > 0:
        print ("Lowest Price : ",it.lowest_price)
    else:
        print ('No valid price found!')
    if volume and len(it.volume) > 0:
        print ("Volume :" ,it.volume)

PrintMarketItem(GetMarketItem('Nova | Polar Mesh' + FT), True)