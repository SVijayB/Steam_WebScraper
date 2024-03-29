from urllib.request import Request, urlopen
import json
import time
from re import sub
import re
from Modules.Colours import *


def currency(price):
    print()
    req = Request('https://api.ratesapi.io/api/latest', headers={'User-Agent': 'Mozilla/5.0'})
    url = urlopen(req).read()
    data = json.loads(url)
    rates = data["rates"]
    rates = str(rates)

    value = re.findall(r": (.*?),", rates)
    currency = re.findall(r"'(.*?)'", rates)

    cyan("CURRENCY : ")
    for x in range(len(currency) - 1):
        print(x + 1, currency[x])
        time.sleep(0.000025)
    yellow("Pick your currency type")
    choice = 0
    while choice < 1 or choice > 31:
        try:
            choice = int(input("> "))
            if choice < 1 or choice > 31:
                raise ValueError
        except ValueError:
            red("ERROR : INVALID NUMBER")

    values = {}
    for num in range(len(value)):
        values[num + 1] = value[num]

    names = {}
    for num in range(len(currency)):
        names[num + 1] = currency[num]

    value = float(values[choice])
    price = float(sub(r"[^\d.]", "", price))
    money = round(price / float(values[30]) * value, 2)
    result = str(money) + " " + (names[choice])
    return result