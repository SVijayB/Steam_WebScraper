import urllib.request
import json
import re

def currency():
    url = urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
    data = json.loads(url.read())
    rates = (data['rates'])
    rates = str(rates)
    currency = re.findall(r"'(.*?)'",rates)
    value = re.findall(r": (.*?),",rates)
    dict = {}
    for currency in currency:
        for value in value:
            dict[currency] = value
    print(dict)
currency()