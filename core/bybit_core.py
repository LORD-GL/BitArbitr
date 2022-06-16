""" 
        TEST API BYBIT 
        11032006Gv
    key: YsEPd7L4ZJioawkYBg
 secret: bcnkPzAajAVOzc3mICXQf25ytpi4LM5rlVCB
"""
def get_price(symbolInp="BTCUSDT"):
    from pybit import inverse_perpetual
    session_unauth = inverse_perpetual.HTTP(
        endpoint="https://api-testnet.bybit.com"
    )
    try:
        return float(session_unauth.latest_information_for_symbol(symbol=symbolInp)['result'][0]['last_price'])
    except:
        return -1

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