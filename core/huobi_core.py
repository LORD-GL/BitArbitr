""" 
        HUOBI API TEST
"""

# from huobi import HuobiRestClient

# client = HuobiRestClient(
#     access_key = "56d2c9bd-67054997-ur2fg6h2gf-d00e4",
#     secret_key = "893b8599-394ee401-7da5f115-0c040"
# )

# price = client.market_history_trade(symbol="btcusdt").data


# print(price['data'][0]['data'][0]['price'])

# def get_price(symbol):
<<<<<<< HEAD
=======
#     print(client.market_history_trade(symbol=symbol).data['data'][0]['data'][0])
>>>>>>> 0b8050ac48e11cc04560f6d039510486349dd868
#     try:
#         if "hotusdt" in symbol:
#             return -1
#         elif "gstusdt" in symbol:
#             return -1
#         return float(client.market_history_trade(symbol=symbol).data['data'][0]['data'][0]['price'])
#     except:
<<<<<<< HEAD
#         return -1
=======
#         return -1 

#https://api.huobi.pro/market/ticker?symbol=btcusdt&AccessKeyId=56d2c9bd-67054997-ur2fg6h2gf-d00e4
# requests.get("https://api.huobi.pro/market/tickers").json()

>>>>>>> 0b8050ac48e11cc04560f6d039510486349dd868

import requests

def get_price(symbol="btcusdt"):
<<<<<<< HEAD
    if "hotusdt" in symbol:
        return -1, -1
    elif "gstusdt" in symbol:
        return -1, -1
=======

>>>>>>> 0b8050ac48e11cc04560f6d039510486349dd868
    resp = requests.get("https://api.huobi.pro/market/tickers").json()
    for i in resp['data']:
        if i['symbol'] == symbol:
            return float(i['close']), round(float(i['amount']), 2)
<<<<<<< HEAD
    return -1, -1
=======
    return -1, -1
>>>>>>> 0b8050ac48e11cc04560f6d039510486349dd868
