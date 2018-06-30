# -*- coding:utf-8 -*-

import json,sys,time
from datetime import datetime as dt

args = sys.argv
tweet_file = args[1]
f = open(tweet_file,'r')
json_dict = json.load(f)
count = 0
neg_flag = False

for i in range(len(json_dict)):
    if count == 0:
        sec = dt.strptime(json_dict[i]['time'],"%d %H:%M:%S").second
    else:
        next_time = dt.strptime(json_dict[i]['time'],"%d %H:%M:%S")
        if(neg_flag == False):
            before_time = dt.strptime(json_dict[i-1]['time'],"%d %H:%M:%S")
        print("before {}".format(before_time))
        print("next {}".format(next_time))
        sec = (next_time-before_time).seconds

        if sec < 0:
            neg_flag = True
        else:
            neg_flag = False
    print("待ち時間 : {}".format(sec))
    if sec > 0:
        time.sleep(sec)
    print(json_dict[i]['name']+'::')
    print("")
    print(json_dict[i]['text'])
    print("")
    print(json_dict[i]['time'])
    print("-------------------------------------------")
    count += 1
"""
for tweet in json_dict:
    created_at = tweet['created_at']
    next_tweet_time = dt.strptime(created_at[11:19],'%H:%M:%S')
    if count == 0:
        print(created_at[17:19])
        time.sleep(int(created_at[17:19]))
    else:
        print("次のコメントまで{}秒".format(next_tweet_time-before_tweet_time))
        time.sleep((next_tweet_time-before_tweet_time).seconds)
    print(tweet['user']['name']+'::'+tweet['text'])
    print(tweet['created_at'])
    count += 1
    before_tweet_time = next_tweet_time
"""
