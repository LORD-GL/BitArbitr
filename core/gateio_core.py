#https://api.gateio.ws/api/v4/spot/currency_pairs/{currency_pair}
import requests
import json
from time import sleep

def get_price(symbol="BTC_USDT"):
    #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    if "USDC" in symbol or "DAI" in symbol:
        return -1, -1
    try:
        resp = requests.get(f"https://api.gateio.ws/api/v4/spot/order_book?currency_pair={symbol}").json()
    except:
        return -1, -1
    try:
        return float(resp['asks'][0][0]), -1
    except:
        return -1, -1

# def get_price(symbol="BTC_USDT"):
#     if "USDC" in symbol or "DAI" in symbol:
#         return -1, -1
#     ans = requests.get(f"https://api.gateio.ws/api/v4/spot/tickers").json()
#     for i in ans:
#         if i['currency_pair'] == symbol:
#             return float(i['last']), round(float(i['base_volume']), 2)
#     return -1, -1