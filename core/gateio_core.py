#https://api.gateio.ws/api/v4/spot/currency_pairs/{currency_pair}
import requests
import json
from time import sleep

def get_price(symbol="BTC_USDT"):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    try:
        resp = requests.get(f"https://api.gateio.ws/api/v4/spot/order_book?currency_pair={symbol}", headers=headers).json()
    except:
        sleep(1)
        resp = requests.get(f"https://api.gateio.ws/api/v4/spot/order_book?currency_pair={symbol}", headers=headers).json()
    try:
        return float(resp['asks'][0][0])
    except:
        return -1
