#https://api.crypto.com/v2/  public/get-instruments
import requests
import json

list_pairs_crypto = []
resp_list = requests.get("https://api.crypto.com/v2/public/get-instruments").json()
for i in resp_list['result']['instruments']:
    list_pairs_crypto.append(i['instrument_name'])


def get_price(symbol="BTC_USDT"):
    if symbol not in list_pairs_crypto:
        return -1, -1
    try:
        resp = requests.get(f"https://api.crypto.com/v2/public/get-ticker?instrument_name={symbol}").json()['result']['data']
        return float(resp['a']), round(float(resp['v']), 2)
    except:
        return -1, -1