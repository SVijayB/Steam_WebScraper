from Modules.MarketItem import MarketItem
from Modules.MarketItem import *
from Modules.Colours import *
from Modules.Data import *
from Modules.Name import *
import os

if __name__ == "__main__":
    os.system("cls")
    logo = open("../assets/logo.txt", "r").read()
    grey(logo)
    green("\n" + "-" * 30)
    data = open("../assets/version.txt", "r").read()
    red("Steam_WebScraper | " + data)
    time.sleep(1)
    main(Result(GetMarketItem(name())))
