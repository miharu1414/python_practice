from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys

"""画像の格納場所"""
file_name =''

"""object_listをいじれば画像のジャンルを変えられる"""

from datetime import datetime
now = datetime.now()
now_time=''
if(5<=now.hour<12):
    now_time = "朝"
elif(12<=now.hour<17):
    now_time = "昼"
else:
    now_time = "夜"

"""session1
夜の飯テロ用画像取得"""
if(now_time=="夜" or now_time=="昼"):
    key_flickapi = "8afa7b5169ff3aa6abfe21f7ef38a9de"
    secret_flickapi = "19e315d51c12be80"
    # 1秒間隔でデータを取得(サーバー側が逼迫するため)
    wait_time = 1

    # コマンドラインの引数の1番目の値を取得。以下の場合は[cat]を取得
    # python download.py cat 

    import random
    if(now_time=="夜"):
        object_list = ["寿司","肉","ラーメン","油そば","飯テロ","高級イタリアン"]
    elif(now_time=="昼"):
        object_list = ["夜景","絶景","名画","sky","ocean","星空"]
    object_name=random.choice(object_list)

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
        per_page = 1000,
        media = 'photos',
        sort = 'relevance',
        safe_seach = 1,
        extras = 'url_q, licence'
    )

    # 結果
    photos = result['photos']
    pprint(photos)
    """

    """
    import requests
    import random


    """原型
    i  =random.randint(0,10)
    photo = photos['photo'][i]
    url_q = photo['url_q']
    file_name = "./images/lunch/"+photo['id'] + '.png'
    """
    photo_list = []
    for i,photo in enumerate(photos['photo']):
        photo_list.append(photo)
    photo = random.choice(photo_list)
    url_q = photo['url_q']

    file_name = "./images/"+photo['id'] + '.png'

    response = requests.get(url_q)
    image = response.content

    with open(file_name, "wb") as f:
        f.write(image)
        f.close()
    """session1終了"""


"""session2　天気の取得"""
import requests
import urllib.parse as parse
import time
from datetime import datetime


token = '4kG90ZpgrUxNMFIYNB7xuQkPUFeXD87qBLKJaTL2mVk'
url = 'https://notify-api.line.me/api/notify'#LINE NotifyのAPIのURL

now = datetime.now() #現在時刻の取得

if(now_time=="朝"):
#天気の取得　https://qiita.com/MonoShobel/items/c36bb0e8eecf538248b4
#bs4　　　https://techacademy.jp/magazine/26426
    import urllib3
    from bs4 import BeautifulSoup

    #アクセスするURL
    url_tenki = 'https://weather.yahoo.co.jp/weather/jp/13/4410.html'

    #URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
    http = urllib3.PoolManager()
    instance = http.request('GET', url_tenki)
    #instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
    soup = BeautifulSoup(instance.data, 'html.parser')

    #CSSセレクターで天気のテキストを取得します。
    #今日の天気
    tenki_today = soup.select_one('#main > div.forecastCity > table > tr > td > div > p.pict')
    tenki_moji = str(tenki_today.text)

    tenki_moji= (''.join(tenki_moji.splitlines())) #余分な前部分？改行の空白を削除
    tenki_moji= tenki_moji.rstrip()
    tenki = "今日の天気は「" +tenki_moji+'」'
    #天気の取得
    """session2 終了"""
\


"""session3 メッセージの送信一回目"""
if(now_time=="朝"):
    ms_data="\nおはよう！朝ですよ～\n"+tenki#メッセージ内容
elif(now_time=="昼"):
    ms_data="\nこんにちは！\nyoutube見てないで，何か勉強しな～"#メッセージ内容
elif(now_time=="夜"):
    ms_data="\nこんばんは！\n記録をちゃんとつけて寝ようね"#メッセージ内容


send_data = {'message': ms_data}#メッセージ
headers = {'Authorization': 'Bearer ' + token}#トークン名



#画像ファイルのパスを指定
image_file = file_name  #'./test.png'


#バイナリデータで読み込む
if image_file == '':
    res = requests.post(url,
                data=send_data,
                headers=headers)

else:
    binary = open(image_file, mode='rb')
    #指定の辞書型にする
    image_dic = {'imageFile': binary}
    #送信
    res = requests.post(url,
                    data=send_data,
                    headers=headers,
                    files = image_dic)
print(f'{ms_data}　と送信')
print(res)#メッセージが送れたかどうかの結果を表示

time.sleep(1)
if(now_time=="朝"):
    ms_data="\n朝活しよう！\nhttps://kenkoooo.com/atcoder/#/table/"

elif(now_time=="昼"):
    ms_data="\nところで今日の『"+object_name+"』はこれだ！"

elif(now_time=="夜"):
    ms_data="\n今夜の飯テロはこれ！\n『"+object_name+"』"


send_data = {'message': ms_data}#メッセージ
headers = {'Authorization': 'Bearer ' + token}#トークン名

res = requests.post(url,
                data=send_data,
                headers=headers)


#画像を削除

time.sleep(4)
"""
import shutil

shutil.rmtree('images/lunch/')
new_dir_path = "images/lunch"
os.mkdir(new_dir_path)
"""
print(f'{ms_data}   と送信')
print(res)#メッセージが送れたかどうかの結果を表示