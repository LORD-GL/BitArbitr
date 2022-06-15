""" 
        EXMO FUNC TEST
"""
import requests
import json

# Получаем данные о текущих сделках и стаканах
def get_ticker(pair):
    url_trades = 'https://api.exmo.me/v1/ticker/'
    ticker = requests.get(url_trades, verify=False) 
    info = ticker.text
    info = json.loads(info) 
    info_pair = info.get(pair) 
    return info_pair 

# price = get_ticker("BTC_USDT")

# print(price['last_trade'])

def get_price(symbol):
    try:
        return float(get_ticker(symbol)['last_trade'])
    except:
        return -1