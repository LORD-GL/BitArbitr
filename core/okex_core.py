import json
import requests
url = 'https://www.okex.com'

def get_price(symbol='BTC-USDT'):
    if "ONE-USDT" in symbol:
        return -1, -1
<<<<<<< HEAD
    try:
        ticker = requests.get(url+'/api/v5/market/ticker?instId='+symbol).json()
    except:
        return -1, -1 
=======
    ticker = requests.get(url+'/api/v5/market/ticker?instId='+symbol).json()
>>>>>>> 0b8050ac48e11cc04560f6d039510486349dd868
    if ticker['code'] == '0':
        return float(ticker['data'][0]['last']), round(float(ticker['data'][0]['vol24h']), 2)
    else:
        return -1, -1
<<<<<<< HEAD
=======


>>>>>>> 0b8050ac48e11cc04560f6d039510486349dd868
