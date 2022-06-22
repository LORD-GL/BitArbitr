import requests
import json

base_url = "https://api.gemini.com/v1"
list_pair_genimi = requests.get(base_url+"/symbols").json()

def get_price(base='btc', quor='usd'):
    if quor == 'dai':
        return -1, -1 
    if base+quor not in list_pair_genimi:
        return -1, -1
    resp = requests.get(base_url+f'/pubticker/{base+quor}').json()
    try:
        return float(resp['last']), round(float(resp['volume'][base.upper()]), 2)
    except:
        return -1, -1