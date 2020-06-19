from Modules.Data import *
from Modules.Name import *
from Modules.MarketItem import MarketItem
from Modules.MarketItem import *

if __name__ == "__main__":
	data = open("../assets/version.txt" , "r").read()
	print("Steam_WebScraper | " + data)
	time.sleep(1)
	main(Result(GetMarketItem(name())))