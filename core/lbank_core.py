import requests
import json


def get_price(symbol="btc_usdt"):
    if symbol == "gmt_usdt":
        symbol = "gmt1_usdt"
    elif "zil_usdt" in symbol:
        return -1
    resp = requests.get(f"https://api.lbkex.com/v2/ticker/24hr.do?symbol={symbol}", verify=False).json()
    try:
        return float(resp['data'][0]['ticker']['latest'])
    except:
        return -1
