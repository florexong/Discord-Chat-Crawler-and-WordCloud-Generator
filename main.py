from email import header
import requests
import json
import pandas as pd
from sqlalchemy import column
from decouple import config

column = ['Text']
df = pd.DataFrame(columns= column)

def retrieve_message(channelid):
    headers ={
        ## The key of authorization
        'authorization': config('key')
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit=100',headers=headers)
    print(r)
    ## Print the status code 200 means success
    jsonn = json.loads(r.text)
    i =0 
    for value in jsonn:
        
        i +=1
        df.loc[i] = value['content']

retrieve_message(config('id'))
df.to_csv('aaaa.csv')