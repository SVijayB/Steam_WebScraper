import re
import time

def skins(wep):
	data = open("assets/Data.txt","r",encoding="utf-8").read()
	item_list = []
	i = 0
	qual = "Battle-Scarred"
	value = re.findall(r": '%s \| (.*?) \(%s\)'" %(wep, qual), data)[0]
	print(len(value))
	if(len(value)>25):
		qual = "Factory New"
	while(True):
		try:
			value = re.findall(r": '%s \| (.*?) \(%s\)'" %(wep, qual), data)[i]
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

skins("FAMAS")