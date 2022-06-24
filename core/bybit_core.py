""" 
        TEST API BYBIT 
        11032006Gv
    key: YsEPd7L4ZJioawkYBg
 secret: bcnkPzAajAVOzc3mICXQf25ytpi4LM5rlVCB
"""
# https://api.bybit.com/v2/spot/v1/symbols
import requests
import json

pairs_bybit = []
resp_bybit = requests.get("https://api.bybit.com/spot/v1/symbols").json()['result']
for i in resp_bybit:
    pairs_bybit.append(i['name'])

def get_price(symbol="BTCUSDT"):
    if symbol not in pairs_bybit:
        return -1, -1
    if "CVX" in symbolInp:
        return -1, -1
    elif "GMT" in symbolInp:
        return -1, -1
    elif "GST" in symbolInp:
        return -1, -1
    resp = requests.get(f"https://api.bybit.com/spot/quote/v1/ticker/24hr?symbol={symbol}").json()['result']
    return float(resp['lastPrice']), round(float(resp['volume']), 2)


# from pybit import inverse_perpetual
# session_unauth = inverse_perpetual.HTTP(
#     endpoint="https://api-testnet.bybit.com"
# )

# def get_price(symbolInp="BTCUSDT"):
#     if "CVX" in symbolInp:
#         return -1, -1
#     elif "GMT" in symbolInp:
#         return -1, -1
#     elif "GST" in symbolInp:
#         return -1, -1
    
#     try:
#         data = session_unauth.latest_information_for_symbol(symbol=symbolInp)
        
#         #print(data)
#         return float(data['result'][0]['last_price']), round( float(data['result'][0]['volume_24h']), 2)
#     except:
#         return -1, -1


# import bybit

# client = bybit.bybit(
#     #test=False,
#     api_key='YsEPd7L4ZJioawkYBg',
#     api_secret='bcnkPzAajAVOzc3mICXQf25ytpi4LM5rlVCB',
# )

# import requests

# param_str = "symbol=BTCUSDT&api_key=YsEPd7L4ZJioawkYBg&timestamp="
# resp = requests.get(f"https://api.bybit.com/v2/private/order?{param_str}")
# print(resp.json()['time_now'])
# print(param_str)
# param_str += str(round(float(resp.json()['time_now'])))
# print(param_str)
# resp = requests.get(f"https://api.bybit.com/v2/private/order?{param_str}")
# # resp2 = requests.get("https://api-testnet.bybit.com/perpetual/usdc/openapi/public/v1/order-book?symbol=BTCPERP")
# print(resp.json())
# print(resp2.json())

# def get_price(symbol="ETHUSDT"):
#     try:
#         return float(client.Market.Market_orderbook(symbol=symbol).result()[0].get('result')[0]['price'])
#     except:
#         return -1

#price = client.Market.Market_orderbook(symbol="ETHUSDT").result()

#client.latest_information_for_symbol(symbol="ETHUSDT").result()

#print("ETH/USDT: ", get_price(symbol = "ETHUSDT"))
# for i in range(50):
# print("BTC/USDT: ", get_price(symbol = "BNBUSDT"))

#print( client.Market.Market_orderbook(symbol="SOLUSDT").result() )
#print( client.Market.symbolInfo().result() )