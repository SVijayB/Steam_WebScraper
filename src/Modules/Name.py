from Steam_WebScraper import *
import json
import time
import re

def name():
	print()
	print("CSGO ITEMS : ")
	for x in range(len(csitems)): 
		print (x+1,csitems[x])
		time.sleep(0.0025)
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
		time.sleep(0.0025)
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
	nm = item_name(csitems[wep])
	final = csitems[wep] + " | " + nm + qualfinal[qual]
	return final

def item_name(wep):
	data = open("../assets/Data.txt","r",encoding="utf-8").read()
	item_list = []
	i = 0
	while(True):
		try:
			value = re.findall(r": '%s \| (.*?) \(%s\)'" %(wep, "Battle-Scarred"), data)[i]
			item_list.append(value)
			i = i + 2
		except:
			break

	print("ITEM SKINS : ")
	for i in range(len(item_list)):
		print((i+1), "\b)" , item_list[i])
		time.sleep(0.0025)
	item = 0

	print("Pick the item skin")
	while (item<1 or item>(len(item_list)+1)):
		try:
			item = int(input("> "))
			if(item<1 or item>(len(item_list)+1)):
				raise ValueError
		except ValueError:
			print("ERROR : INVALID NUMBER")
	item = int(item)-1
	print("\nSelected Skin -", item_list[item])
	return(item_list[item])
	
