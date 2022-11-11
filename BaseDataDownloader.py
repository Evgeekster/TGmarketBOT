import os
import sqlite3
import requests
import wget
import urllib.request, json
import time
import csv

PATH_TO_FOLDER = r'C:\Users\evgen\Desktop\PyTGBot\dbholder'
def Downloader():
   # while True:
    with urllib.request.urlopen("https://market.csgo.com/itemdb/current_730.json") as url:
        data = json.load(url)
        #print(data)
    URL = 'https://market.csgo.com/itemdb/'+data['db']
    PATH_TO_BD = r'C:\Users\evgen\Desktop\PyTGBot\dbholder'+data['db']

    # print(data['db'])
    DB_NAME = data['db']

    for f in os.listdir(PATH_TO_FOLDER):
        if f.endswith(".csv"):
            # continue
            os.remove(os.path.join(PATH_TO_FOLDER, f))

    os.chdir(PATH_TO_FOLDER)
    wget.download(URL)

    with open(DB_NAME, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=";")
        for row in file_reader:
            pass
                # if 'AWP' in row['c_market_hash_name']:
                #     print(row['c_market_hash_name'])
                #print(row['c_market_hash_name'])                    #получение hash-name из БД файла
       #     time.sleep(60)
