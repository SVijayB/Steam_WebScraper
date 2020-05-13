from Steam_WebScraper import *
def name():
	try:
		for x in range(len(csitems)): 
			print (x+1,csitems[x])
		wep = input("Pick the number that matches the Item you are looking for : ")
		wep = int(wep)-1
		print("Selected Item :",csitems[wep])
		for x in range(len(quality)): 
			print (x+1,quality[x])
		qual = input("Pick the Quality of skin you are looking for : ")
		qual = int(qual)-1
		print("Selected Quality :",quality[qual])
		nm = input("Enter the name of the skin you are looking for(Has to match steam DataBase) : ")
		final = csitems[wep]+" | "+nm+qualfinal[qual]
		return final
	except:
		print("\nERROR : WRONG CHOICE")
		print("Check Spelling and Pick the right Numbers!")
		print("PROGRAM TERMINATED")
		sys.exit(0)