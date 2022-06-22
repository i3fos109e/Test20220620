import json
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('/home/i3fos109e/vibrant-period-353301-1fd1b4796f74.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
collection_ref = db.collection("twodata")

s1 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/315078?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s2 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/251539?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s3 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/312605?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s4 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369297?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s5 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/313567?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s6 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369298?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s7 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369299?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s8 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/315040?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s9 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369301?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s10 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369300?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s11 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369302?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s12 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/312591?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s13 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369303?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s14 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/314999?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s15 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/313812?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s16 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369304?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s17 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369296?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s18 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369306?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s19 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369305?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s20 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369307?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s21 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/2332525?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s22 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369309?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'

source = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22]

for i in range(len(source)):
    response = requests.get(source[i])
    data = json.loads(response.text)
    # print(data)
    for j in range(len(data)):
        collection_ref.add(data[j])


