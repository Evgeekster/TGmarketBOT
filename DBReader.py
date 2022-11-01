# from BaseDataDownloader import DB_NAME, PATH_TO_FOLDER
import json, csv
import os
from BaseDataDownloader import Downloader, PATH_TO_FOLDER

Downloader()
name_db = os.listdir(PATH_TO_FOLDER)[0]
print(name_db)
WEAPON = 'AK-47'
weaps = set()
price = set()
def ReadDB(weapon):

    with open(name_db, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=";")
        for row in file_reader:
            if weapon in row['c_market_hash_name']:
                 weaps.add(row['c_market_hash_name'])
    return weaps


# print(ReadDB('AWP'))