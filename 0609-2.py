from imp import source_from_cache
import json
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('/home/i3fos109e/vibrant-period-353301-1fd1b4796f74.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
collection_ref = db.collection("onedata")

s1 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-001?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s2 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-005?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s3 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-009?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s4 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-013?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s5 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-017?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s6 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-021?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s7 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-025?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s8 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-029?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
s9 = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-033?Authorization=CWB-025D81F9-BD99-4E50-BA59-5D9878B4BEE9'
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

source = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22]

for i in range(len(source)):
    response = requests.get(source[i])
    data = json.loads(response.text)
    collection_ref.add(data)

