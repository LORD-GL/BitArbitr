# from pykrakenapi import KrakenAPI
# import krakenex
import json
import requests
# api = krakenex.API(
#     "zvbJiVkUQpgS5si+Rcr+9lyOb/uQMlqLmr0bL5+dBoyXaxPQJimfx2gn",
#     "SYtAZKfKCjOZubndbUGEN+CR9LJxC2s0iXHuO9tO1X1L7FIHlvwx+kzQwQ6yi9SAotV/Fom7ED/cskYveg3y5w=="
# )
# k = KrakenAPI(api)
def get_price(symbol="BTCUSDT"):
    # try:
    #     a = k.get_ticker_information(symbol)
    #     return round( float(a.loc[:, 'c'][0][0]), 4)
    # except:
    #     return -1
    resp = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={symbol}', verify=False).json()
    try:
        if "BTCUSDT" == symbol:
            return round( float(resp['result']['XBTUSDT']['c'][0]), 4)
        return float(resp['result'][symbol]['c'][0])
    except:
        return -1
