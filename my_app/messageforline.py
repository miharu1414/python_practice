import requests
import urllib.parse as parse
import time
from datetime import datetime



token = '4kG90ZpgrUxNMFIYNB7xuQkPUFeXD87qBLKJaTL2mVk'
url = 'https://notify-api.line.me/api/notify'#LINE NotifyのAPIのURL

now = datetime.now() #現在時刻の取得




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





if(5<=now.hour<12):
    ms_data="\nおはよう！朝ですよ～\n朝活しよう！\n"+tenki#メッセージ内容
elif(12<= now.hour < 17):
    ms_data="\nこんにちは！\nyoutube見てないで，何か勉強しな～\nhttps://kenkoooo.com/atcoder/#/table/"#メッセージ内容
elif(17<= now.hour < 24 or now.hour<5):
    ms_data="\nこんばんは！\n記録をちゃんとつけて寝ようね"#メッセージ内容


send_data = {'message': ms_data}#メッセージ
headers = {'Authorization': 'Bearer ' + token}#トークン名


#画像ファイルのパスを指定
image_file = './test.png'
#バイナリデータで読み込む
if image_file != '':
    #送信
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
if(5<=now.hour<12):
    ms_data="\nhttps://kenkoooo.com/atcoder/#/table/"
elif(12<=now.hour<17):
    ms_data=" "
elif(17<=now.hour or now.hour<5):
    ms_data=" "
send_data = {'message': ms_data}#メッセージ
headers = {'Authorization': 'Bearer ' + token}#トークン名


#画像ファイルのパスを指定
image_file = './test.png'
#バイナリデータで読み込む
if image_file != '':
    #送信
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
print(res)#メッセージが送れたかどうかの結果を表示