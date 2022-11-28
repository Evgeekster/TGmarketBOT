import json, csv
import os
from BaseDataDownloader import Downloader, PATH_TO_FOLDER
from config import API
from AllSkinStuff import allskins
CLASSID = ''
INSTANCEID = ''
PRICE = ''
HASH = ''
URL = 'https://market.csgo.com/api/Buy/' + CLASSID + '_'+ INSTANCEID + '/'+PRICE+'/'+HASH + '/?key=' + API
def BuyItem(class_id, inst_id, price, hash):

    pass


