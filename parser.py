import json
import requests
from bs4 import BeautifulSoup as BS
from config import API
HOST = 'https://market.csgo.com/'
URL = 'https://market.csgo.com/api/QuickItems/?key='+API
from config import HEADERS


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='market-items')
    return items

html = get_html(URL)
with open('result.json', 'w') as file:
    json.dump(html.json(), file, indent=4, ensure_ascii=False)



