from urllib.request import urlopen
from json import loads
from datetime import datetime
import sys
import json

def last_updated_on():
    date = open("../assets/LastUpdatedOn.txt","r")
    DateAndTime = date.read()
    if(len(DateAndTime)!=0):
        print("Last Updated On " + DateAndTime)
    date.close()

def last_time_update():
    date = open("../assets/LastUpdatedOn.txt","w")
    now = datetime.now()
    DateAndTime = now.strftime("%d/%m/%Y %H:%M:%S")
    date.write(DateAndTime)
    date.close()

def update():
    try:
        url = urlopen("http://csgobackpack.net/api/GetItemsList/v2/?no_prices=yes&no_details=yes&details=no&prettyprint=yes")
        data = json.loads(url.read())
        strdata = str(data)
        path = "../assets/Data.txt"
        with open(path,"w",encoding="utf-8") as f:
            f.write(strdata)
        f.close()
    except:
        print("API RESPONSE ERROR...\nTry again in a while.")
        input("Press any key to exit ")
        sys.exit(0)

if __name__ == "__main__":
    last_updated_on()
    choice = input("Would you like to update current local data?(Y/n)\n> ").lower()
    while True:
        if(choice=="y" or choice=="yes"):
            break
        elif(choice=="n" or choice=="no"):
            print("Thanks for using Steam_WebScraper")
            input("Press any key to exit ")
            sys.exit(0)
        else:
            choice = input("Pick the correct option\n> ")
            continue
    print("Update Process Started...\nThis might take a while. We will notify you once it is done.")
    update()
    last_time_update()
    print("Data has been successfully updated!")
    input("Press any key to exit ")