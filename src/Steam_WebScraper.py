from Modules.data import *
from Modules.name import *
from Modules.MarketItem import MarketItem
from Modules.MarketItem import *

if __name__ == "__main__":
	data = open("../version.txt" , "r").read()
	print("Steam_WebScraper | " + data)
	time.sleep(1)
	main(Result(GetMarketItem(name())))