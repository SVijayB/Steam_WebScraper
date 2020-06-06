from Steam_WebScraper import *
import time

def name():
	print()
	print("CSGO ITEMS : ")
	for x in range(len(csitems)): 
		print (x+1,csitems[x])
		time.sleep(0.000025)
	print("Pick the number that matches the Item you are looking for")
	wep = 0
	while (wep<1 or wep>53):
		try:
			wep = int(input("> "))
			if(wep<1 or wep>53):
				raise ValueError
		except ValueError:
			print("ERROR : INVALID NUMBER")
	wep = int(wep)-1
	print("\nSelected Item -",csitems[wep]+"\n")

	print("ITEM QUALITY : ")
	for x in range(len(quality)): 
		print (x+1,quality[x])
	print("Pick the Quality of skin you are looking for")
	qual = 0
	while (qual<1 or qual>5):
		try:
			qual = int(input("> "))
			if(qual<1 or qual>5):
				raise ValueError
		except ValueError:
			print("ERROR : INVALID NUMBER")
	qual = int(qual)-1
	
	print("\nSelected Quality -",quality[qual]+"\n")
	nm = input("Enter the name of the skin you are looking for (Has to match Steam DataBase)\n> ")
	final = csitems[wep]+" | "+nm+qualfinal[qual]
	return final
