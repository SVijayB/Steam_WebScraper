from Steam_WebScraper import *
from Modules.Skins import skins
import time


def name():
    print()
    cyan("CSGO ITEMS : ")
    for x in range(len(csitems)):
        print(x + 1, csitems[x])
        time.sleep(0.0025)
    yellow("Pick the number that matches the Item you are looking for")
    wep = 0
    while wep < 1 or wep > 34:
        try:
            wep = int(input("> "))
            if wep < 1 or wep > 34:
                raise ValueError
        except ValueError:
            red("ERROR : INVALID NUMBER")
    wep = int(wep) - 1
    green("\nSelected Item - " + str(csitems[wep]) + "\n")

    cyan("ITEM QUALITY : ")
    for x in range(len(quality)):
        print(x + 1, quality[x])
        time.sleep(0.0025)
    yellow("Pick the Quality of skin you are looking for")
    qual = 0
    while qual < 1 or qual > 5:
        try:
            qual = int(input("> "))
            if qual < 1 or qual > 5:
                raise ValueError
        except ValueError:
            red("ERROR : INVALID NUMBER")
    qual = int(qual) - 1

    print("\nSelected Quality - " + str(quality[qual]) + "\n")
    nm = skins(csitems[wep])
    final = csitems[wep] + " | " + nm + qualfinal[qual]
    return final
