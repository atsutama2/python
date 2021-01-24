import requests
from bs4 import BeautifulSoup

target_url = 'http://ogitaiweb.main.jp/ogitaiclub/'
r = requests.get(target_url)
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

# 全てのaタグを取得し、リンク先URL（href属性）を表示
for a in soup.find_all('a'):
      print(a.get('href')) 