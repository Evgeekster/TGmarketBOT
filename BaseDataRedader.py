import os
import sqlite3
import requests
import wget
import urllib.request, json
with urllib.request.urlopen("https://market.dota2.net/itemdb/current_570.json") as url:
    data = json.load(url)
    print(data)
URL = 'https://market.dota2.net/itemdb/'+data['db']
PATH = r'C:\Users\evgen\Desktop\PyTGBot\dbholder'
print(data['db'])

wget.download(URL)

# with open(os.path.join(PATH,wget.download(URL)), "w") as file1:
#     file1.write(wget.download(URL))