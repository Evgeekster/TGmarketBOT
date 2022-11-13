# from BaseDataDownloader import DB_NAME, PATH_TO_FOLDER
import json, csv
import os
from BaseDataDownloader import Downloader, PATH_TO_FOLDER

Downloader()
name_db = os.listdir(PATH_TO_FOLDER)[0]

weaps = set()

def ReadDB(weapon):

    with open(name_db, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=";")
        for row in file_reader:
            if weapon in row['c_market_hash_name']:
                 weaps.add(row['c_market_hash_name'])
    return weaps

def get_url(weapon):
    with open(name_db, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=";")
        url_frog = 'https://market.csgo.com/item/'
        for row in file_reader:
            if weapon in row['c_market_hash_name']:
                # links.add
                return (url_frog + str(row['c_classid']) + '-' + str(row['c_instanceid']) + '-' + str(row['c_market_hash_name'].replace(' ', '').replace('(', '').replace(')', '').replace('™', '').replace("'", '')) + '/')

def get_rairty(weapon):
    with open(name_db, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=";")
        for row in file_reader:
            if weapon in row['c_market_hash_name']:
                return str(row['c_rarity'])


