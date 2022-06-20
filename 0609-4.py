import json
import requests
import pymongo


s01 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/315078?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s02 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/251539?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s03 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/312605?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s04 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369297?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s05 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/313567?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s06 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369298?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s07 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369299?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s08 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/315040?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
s09 ='http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/3369301?apikey=IOGX2VpQDutEmY8RvEd5jR3YqPrGf2Wx&language=zh-tw'
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


source = [s01,s02,s03,s04,s05,s06,s07,s08,s09,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22]

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["weather"]
collection = db["twodata"]

data ={}
for i in range(len(source)):
    response = requests.get(source[i])
    data = json.loads(response.text)
    # print(data)
    collection.insert_many(data)

