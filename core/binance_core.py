""" 
        BINANCE API TEST
        Artem owner
"""

import requests
import time

list_p = []
respond = requests.get("https://api.binance.com/api/v1/exchangeInfo").json()
for i in respond['symbols']:
       list_p.append(i['symbol'])

def get_price(symbol="BTCUSDT"):
        if symbol not in list_p:
                return -1, -1
        resp = requests.get(f"https://api.binance.com/api/v1/ticker/24hr?symbol={symbol}").json()
        try:
                if resp['lastid'] == -1: return -1, -1
                return float(resp['lastPrice']), round(float(resp['volume']), 2)
        except:
                return -1, -1
