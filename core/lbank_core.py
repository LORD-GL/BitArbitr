import requests
import json


def get_price(symbol="btc_usdt"):
    if symbol == "gmt_usdt":
        symbol = "gmt1_usdt"
    elif "zil_usdt" in symbol:
        return -1, -1
    elif "shib" in symbol:
        return -1, -1
    elif "ada" in symbol:
        return -1, -1
    try:
        resp = requests.get(f"https://api.lbkex.com/v2/ticker/24hr.do?symbol={symbol}", timeout=3).json()
    except:
        return -1, -1
    try:
        return float(resp['data'][0]['ticker']['latest']), round(float(resp['data'][0]['ticker']['vol']), 2)
    except:
        return -1, -1
        