import json
import requests
url = 'https://www.okex.com'

def get_price(symbol='BTC-USDT'):
    ticker = requests.get(url+'/api/v5/market/ticker?instId='+symbol).json()
    if ticker['code'] == '0':
        return float(ticker['data'][0]['last'])
    else:
        return -1
