# _*_ coding:utf-8 _*_

import json,sys
import datetime as dt
from requests_oauthlib import OAuth1Session

#各種キーをセット
CK = '2g0oC8mdtEDAx5xSpkA4HDZv2'
CS = 'qTII7GXNYWuNwLInHARmRwzjF4iMPW5iHgxcTUXBMRTztTfD4s'
AT = '728159306-BCwLVM4rUzlNbHVMZ9BKjoNzsRCOx8dhnRFePTl1'
ATS = 'wYwKU1DTwXLplEnabGKyRmSkwjV1l6RujPGx16CT1SlJG'
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/search/tweets.json"

keyword = input("検索ワードは? >> ")
start_time = input("検索開始したい yy-mm-dd_hh:mm:ss >> ")
end_time = input("検索終了 yy-mm-dd_hh:mm:ss >> ")
f_name = input("保存ファイル名は？(.json) >> ")
file_name = f_name+".json" 

s_time = dt.datetime.strptime(start_time,"%Y-%m-%d_%H:%M:%S")
e_time = dt.datetime.strptime(end_time,"%Y-%m-%d_%H:%M:%S")

duration = int((e_time-s_time).total_seconds()/60)
print("対象時間は {} 分です".format(duration))

since_time = e_time - dt.timedelta(minutes=1)
until_time = e_time
new_json_dict = []

for i in range(duration):
    # 一分ずつfor文を回す。表示順の都合のためuntil_timeから減らしていく
    since = str(since_time.year)+"-"+str(since_time.month)+"-"+str(since_time.day)+"_"+str(since_time.hour)+":"+str(since_time.minute)+":"+str(since_time.second)
    until = str(until_time.year)+"-"+str(until_time.month)+"-"+str(until_time.day)+"_"+str(until_time.hour)+":"+str(until_time.minute)+":"+str(until_time.second)
    params = {'q' : keyword, 'count' : 200, 'since' : since+'_JST', 'until' : until+'_JST'}

    req = twitter.get(url, params= params)
    if req.status_code == 200:
        jsonData = json.loads(req.text)
        json_dict = jsonData['statuses']
        # 使うものだけ抽出
    
        for j in range(len(json_dict)):
            user_name = json_dict[j]["user"]["name"]
            comment = json_dict[j]["text"]
            created_at = json_dict[j]["created_at"][8:19]
            time = created_at
            new_json_dict.insert(0,{"name":user_name, "text":comment, "time":time})
        
        print("json_dict size is {}".format(len(json_dict)))
    else:
        print("ERROR: {}".format(req.status_code))
    since_time -= dt.timedelta(minutes=1)
    until_time -= dt.timedelta(minutes=1)

#f = open(file_name, 'w')
f = open(file_name, 'w')
json.dump(new_json_dict,f,ensure_ascii=False)
