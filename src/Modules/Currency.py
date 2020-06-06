import urllib.request
import json
import time
from re import sub
import re

def currency(price):
    url = urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
    data = json.loads(url.read())
    rates = (data['rates'])
    rates = str(rates)

    value = re.findall(r": (.*?),", rates)
    currency = re.findall(r"'(.*?)'", rates)

    for x in range(len(currency)-1): 
        print (x+1,currency[x])
        time.sleep(0.000025)

    values = {}
    for num in range(len(value)):
            values[num+1] = value[num]
    
    names = {}
    for num in range(len(currency)):
            names[num+1] = currency[num]
        
    print()
    choice = int(input("\nPick your currency type \n> "))
    value = float(values[choice])
    price = float(sub(r'[^\d.]', '', price))
    money = round(price/float(values[27])*value,2)
    result = str(money) + " " + (names[choice])
    return(result)