import json
import logging
import requests
from bs4 import BeautifulSoup as BS
import csv

HOST = 'https://market.dota2.net/'
URL = 'https://market.dota2.net/api/v2/search-list-items-by-hash-name-all?key=43nf8W19L18k1wVUc64lQrgIqpVzhbM&extended=1&list_hash_name[]=Origins of Faith'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.3.886 Yowser/2.5 Safari/537.36'
}
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='market-items')


html = get_html(URL)
with open('result.json', 'w') as file:
    json.dump(html.json(), file, indent=4, ensure_ascii=False)



