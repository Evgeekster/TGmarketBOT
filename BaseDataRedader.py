import os
import sqlite3
import requests
import wget
import urllib.request, json
import time
while True:
    with urllib.request.urlopen("https://market.dota2.net/itemdb/current_570.json") as url:
        data = json.load(url)
        print(data)
    URL = 'https://market.dota2.net/itemdb/'+data['db']
    PATH_TO_BD = r'C:\Users\evgen\Desktop\PyTGBot\dbholder'+data['db']
    PATH_TO_FOLDER = r'C:\Users\evgen\Desktop\PyTGBot\dbholder'
    print(data['db'])
    DB_NAME = data['db']

    for f in os.listdir(PATH_TO_FOLDER):
        if not f.endswith(".csv"):
            continue
        os.remove(os.path.join(PATH_TO_FOLDER, f))

    os.chdir(PATH_TO_FOLDER)
    wget.download(URL)
    time.sleep(60)