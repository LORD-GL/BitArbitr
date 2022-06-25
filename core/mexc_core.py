#https://api.mexc.com/api/v3/exchangeInfo
import requests
import json 

list_pairs_mexc = []
resp_list_symb = requests.get("https://api.mexc.com/api/v3/exchangeInfo").json()['symbols']

for i in resp_list_symb:
    list_pairs_mexc.append(i['symbol'])

def get_price(symbol="BTCUSDT"):
    if symbol not in list_pairs_mexc:
        return -1, -1
    resp = requests.get(f"https://api.mexc.com/api/v3/ticker/24hr?symbol={symbol}").json()
    try:
        return float(resp['lastPrice']), round(float(resp['volume']), 2)
    except:
        return -1, -1
