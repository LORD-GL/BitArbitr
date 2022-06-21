import json
import requests

def get_price(symbol="BTCUSDT"):
    try:
        resp = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={symbol}').json()
    except:
        return -1, -1
    try:
        if "BTCUSDT" == symbol:
            # print(resp['result']['XBTUSDT']['v'][1])
            return float(resp['result']['XBTUSDT']['c'][0]), round(float(resp['result']['XBTUSDT']['v'][1]), 2)
        return float(resp['result'][symbol]['c'][0]), round(float(resp['result'][symbol]['v'][1]), 2)
    except:
        return -1, -1
