import json
import requests

def get_price(symbol="BTCUSDT"):
    if symbol == "GSTUSDT":
        return -1, -1
    resp = requests.get(f"https://api.phemex.com/md/spot/ticker/24hr?symbol=s{symbol}").json()
    try:
        return float(resp['result']['lastEp']/100000000), round(float(resp['result']['volumeEv']/100000000), 2)
    except:
        return -1, -1
