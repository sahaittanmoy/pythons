#!python
#Run from Command Prompt - not IDLE. Python 3.5.2

import requests, re, urllib, os, json
from bs4 import BeautifulSoup

try:
    headert = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'};
    imgname = "";
    brand = input(u"\nEnter Brand Names seperated by Comma: ").split(",");
    if (input("Type h for higher reolution, or leave blank for best match: ") == 'h'):
        schtyp = "+brand+logo&tbm=isch&tbs=isz:m";
    else:
        schtyp = "+brand+logo&tbm=isch";

    if not os.path.exists("Logos/"):
        os.makedirs("Logos/");
    
    for idx, bname in enumerate(brand):
        r = requests.get("https://www.google.com/search?q="+urllib.parse.quote_plus(bname)+schtyp, headers=headert);
        soup = BeautifulSoup(r.text,"html.parser");

        for lru in soup.find_all('div'):
            if (lru.get('class') is not None and lru.get('class')[0] == 'rg_meta'):
                imgname = lru.contents;
                break;

        ctlist = json.loads(str(imgname[0]));
        imgurl = ctlist['ou'];
        
        urllib.request.urlretrieve(imgurl, "Logos/"+re.sub('[^A-Za-z0-9]+', '', bname)+".jpg")
        print("Downloading Logos:", (idx + 1) * "##", "[%d%%]\r"% (round((idx+1) * (100 / len(brand)),1)), end="") 
except:
    print("Invalid input. Exiting...")
    raise
    
