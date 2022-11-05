# from BaseDataDownloader import DB_NAME, PATH_TO_FOLDER
import json, csv
import os
from BaseDataDownloader import Downloader, PATH_TO_FOLDER

Downloader()
name_db = os.listdir(PATH_TO_FOLDER)[0]
# print(name_db)
WEAPON = 'AK-47'
weaps = set()
price = set()
links = []
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

                links.append(url_frog + str(row['c_classid']) + '-' + str(row['c_instanceid']) + '-' + str(row['c_market_hash_name'].replace(' ', '').replace('(', '').replace(')', '').replace('™', '').replace("'", '')) + '/')

        return links

# def get_url(data):
#     url_pattern = 'https://market.csgo.com/en/item/[4302244430]-[480085569]-[AK-47%20%7C%20Redline%20(Field-Tested)]/'
#     hash_name_arr = data['market_hash_name'].split()
#     hash_name = ''
#     for i in range(len(hash_name_arr)):
#         hash_name += hash_name_arr[i]
#         hash_name += '%20'
#     url = 'https://market.csgo.com/en/item/'+str(data['class'])+'-'+str(data['instance'])+'-'+hash_name + '/'
#
#     return url

# print(ReadDB('AWP'))