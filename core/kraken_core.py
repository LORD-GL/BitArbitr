import json
import requests

def get_price(symbol="BTCUSDT"):
<<<<<<< HEAD
    try:
        resp = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={symbol}').json()
    except:
        return -1, -1
=======
    # try:
    #     a = k.get_ticker_information(symbol)
    #     return round( float(a.loc[:, 'c'][0][0]), 4)
    # except:
    #     return -1
    resp = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={symbol}').json()
>>>>>>> 0b8050ac48e11cc04560f6d039510486349dd868
    try:
        if "BTCUSDT" == symbol:
            # print(resp['result']['XBTUSDT']['v'][1])
            return float(resp['result']['XBTUSDT']['c'][0]), round(float(resp['result']['XBTUSDT']['v'][1]), 2)
        return float(resp['result'][symbol]['c'][0]), round(float(resp['result'][symbol]['v'][1]), 2)
    except:
        return -1, -1
<<<<<<< HEAD
=======

>>>>>>> 0b8050ac48e11cc04560f6d039510486349dd868
