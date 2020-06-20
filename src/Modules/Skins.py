import re
import time

def skins(wep):
	data = open("assets/Data.txt","r",encoding="utf-8").read()
	i = 0
	qual = "Battle-Scarred"
	if(wep=="Bayonet"):
		value = re.findall(r"%s \| (.*?) \(%s\)'" %(wep,qual), data)[0]
		i = 1
	else:
		value = re.findall(r": '%s \| (.*?) \(%s\)'" %(wep, qual), data)[0]
		
	if(len(value)>25):
		qual = "Factory New"

	item_list = searching(wep,qual,i)

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

def searching(wep,qual,i=0):
	data = open("assets/Data.txt","r",encoding="utf-8").read()
	item_list = []
	while(True):
		try:
			if(wep=="Bayonet"):
				value = re.findall(r"%s \| (.*?) \(%s\)'" %(wep,qual), data)[i]
				if(len(value)>25):
					break
			else:
				value = re.findall(r": '%s \| (.*?) \(%s\)'" %(wep, qual), data)[i]
			item_list.append(value)
			i = i + 2
		except:
			break
	return item_list

skins("Bayonet")