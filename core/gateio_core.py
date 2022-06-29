#https://api.gateio.ws/api/v4/spot/currency_pairs/{currency_pair}
import requests
import json
import time

pairs_gate = []
list_resp_gate = requests.get(f"https://api.gateio.ws/api/v4/spot/currency_pairs").json()
for i in list_resp_gate:
    pairs_gate.append(i['id'])


# def get_price(symbol="BTC_USDT"):
#     #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
#     if "USDC" in symbol or "DAI" in symbol:
#         return -1, -1
#     try:
#         resp = requests.get(f"https://api.gateio.ws/api/v4/spot/order_book?currency_pair={symbol}", timeout=3).json()
#     except:
#         return -1, -1
#     try:
#         return float(resp['asks'][0][0]), -1
#     except:
#         return -1, -1

def get_price(symbol="BTC_USDT"):
    if symbol not in pairs_gate:
        return -1, -1
    elif "USDC" in symbol or "DAI" in symbol:
        return -1, -1
    try:
        ans = requests.get(f"https://api.gateio.ws/api/v4/spot/tickers?currency_pair={symbol}").json()[0]
    except:
        return -1, -1
    return float(ans['last']), round(float(ans['base_volume']), 2)
    
# start = time.time()
# print(get_price())
# print(time.time() - start)
# print("----------")
# start = time.time()
# print(get_price_two())
# print(time.time() - start)