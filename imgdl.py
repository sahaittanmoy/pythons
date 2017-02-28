#!python
#Run from Command Prompt - not IDLE

import requests, re, urllib, os
from bs4 import BeautifulSoup

try:
    brand = input(u"\nEnter Brand Names seperated by Comma: ").split(",");

    if not os.path.exists("Logos/"):
        os.makedirs("Logos/");
    
    for idx, bname in enumerate(brand):
        r = requests.get("https://www.google.com/search?q="+urllib.parse.quote_plus(bname)+"+brand+logo&tbm=isch");
        soup = BeautifulSoup(r.text,"html.parser")
        imgurl = (soup.find('img').get('src'));

        urllib.request.urlretrieve(imgurl, "Logos/"+re.sub('[^A-Za-z0-9]+', '', bname)+".jpg")

        print("Downloading Logos:", (idx + 1) * "##", "[%d%%]\r"% (round((idx+1) * (100 / len(brand)),1)), end="") 
except:
    print("Invalid input. Exiting...")
    raise
    
