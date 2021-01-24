# -*- coding: utf-8 -*-

import requests
import json

url = 'http://ogitaiweb.main.jp/ogitaiclub/'
# リクエスト
res = requests.get(url)

#values = json.loads(res.text)
# レスポンスの「Content-Type」がjson形式ではない
print(res.text)