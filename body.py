import tweepy
import logging
import time
import random
from datetime import datetime, timedelta
import schedule
import json
import urllib
from datetime import date
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from config import create_api
api = create_api()





def tweet_a_tweet(api):
    print('inside loop')
    json_obj = urllib.request.urlopen('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = json.load(json_obj)
    old =data['bpi']['USD']['rate_float']
    value1 = old
    while(True):
        time.sleep(24*60*60)
        json_obj = urllib.request.urlopen('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = json.load(json_obj)
        new =data['bpi']['USD']['rate_float']
        value2 = new
        per = ((value2-value1)/value1)*100
        rate = data['bpi']['USD']['rate_float']
        rate = round(rate,2)
        timeer = date.today()
        try:
            api.update_status(str(timeer) + '  #bitcoin ( '+ str(round(per,2))+ '% ): '+str(rate)+'$ ')
            print(str(timeer) + '  #bitcoin ( '+ str(round(per,2))+ ' ): '+str(rate)+'$ ')
        except:
            print('error')
            #api.update_status('')
        
        value1=value2
schedule.every().day.at('00:01').do(tweet_a_tweet(api))
            
while (True):
    schedule.run_pending()
    print('running')
    #tweet_a_tweet(api)
    time.sleep(10)





