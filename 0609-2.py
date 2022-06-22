from imp import source_from_cache
import json
import requests
import pymongo

s01 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-001?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s02 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-005?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s03 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-009?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s04 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-013?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s05 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-017?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s06 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-021?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s07 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-025?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s08 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-029?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s09 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-033?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s10 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-037?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s11 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-041?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s12 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-045?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s13 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-049?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s14 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-053?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s15 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-057?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s16 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-061?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s17 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-065?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s18 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-069?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s19 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-073?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s20 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-077?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s21 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-081?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s22 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-085?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'

source = [s01,s02,s03,s04,s05,s06,s07,s08,s09,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22]

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["weather"]
collection = db["onedata"]

for i in range(len(source)):
    response = requests.get(source[i])
    data = json.loads(response.text)
    collection.insert_one(data)

