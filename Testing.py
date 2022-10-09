import pandas as pd
import requests as rq
import json


myIP_api_url = 'https://api.ipify.org?format=json'

r = rq.get('https://api.ipify.org?format=json')

myIP_dict = r.json()

myIP = myIP_dict['ip']


ipInfo_api_url = f'https://ipinfo.io/{myIP}/geo'


r = rq.get(ipInfo_api_url)

ipInfo_dict = r.json()
ipInfo_df = pd.json_normalize(ipInfo_dict)

myLocation = ipInfo_df['loc'].values[0]

