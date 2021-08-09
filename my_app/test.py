from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys


key_flickapi = "8afa7b5169ff3aa6abfe21f7ef38a9de"
secret_flickapi = "19e315d51c12be80"
# 1秒間隔でデータを取得(サーバー側が逼迫するため)

wait_time = 1

# コマンドラインの引数の1番目の値を取得。以下の場合は[cat]を取得
# python download.py cat 
object_name = "meat"
savedir = "./"+object_name


# format:受け取るデータ(jsonで受け取る）
flickr = FlickrAPI(key_flickapi, secret_flickapi, format='parsed-json')

"""
text : 検索キーワード
per_page : 取得したいデータの件数
media : 検索するデータの種類
sort : データの並び
safe_seach :　UIコンテンツの表示有無
extras : 取得したいオプションの値(url_q 画像のアドレス情報)
"""
result  = flickr.photos.search(
    text = object_name,
    per_page = 1,
    media = 'photos',
    sort = 'relevance',
    safe_seach = 1,
    extras = 'url_q, licence'
)

# 結果
photos = result['photos']
pprint(photos)
"""
for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'

   # 重複したファイルが存在する場合スキップする。
    if os.path.exists(filepath):
        continue
   # 画像データをダウンロードする
    urlretrieve(url_q, filepath)
   # サーバーに負荷がかからないよう、1秒待機する
    time.sleep(wait_time)
"""
import requests
for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    file_name = "./images/lunch/"+photo['id'] + '.jpg'

    response = requests.get(url_q)
    image = response.content

    with open(file_name, "wb") as f:
        f.write(image)
