import math
import sys
import requests
from bs4 import BeautifulSoup 

res = requests.get('https://www.nap-camp.com/shimane/list?sortId=21&pageId=1')

soup = BeautifulSoup(res.text, 'html.parser')

title_text = soup.find('title').get_text()
print(title_text)

links = [url.get('href') for url in soup.find_all('a')]
print(links)

quote_elms = soup.find_all('div', {'class': 'quote'})
print(len(quote_elms))

# CSS セレクターを使って author を全て取得する
author_names = [n.get_text() for n in soup.select('div.quote small.author')]
print(author_names)

def get_piyo_text():
  piyo = soup.select_one('div.hoge div.fuga div.piyo')
  if not piyo:
      return None
  return piyo.get_text()