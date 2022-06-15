import json
import requests

def get_price(symbol="BTCUSDT"):
    resp = requests.get(f"https://api.phemex.com/md/orderbook?symbol=s{symbol}").json()
    try:
        return float(resp['result']['book']['asks'][0][0]/100000000)
    except:
        return -1

# pairs = [["ETH", "USDT"], ["BTC", "USDT"],
#         ["USDC", "USDT"], ["BNB", "USDT"],
#         ["ADA", "USDT"], ["XRP", "USDT"],
#         ["BUSD", "USDT"], ["SOL", "USDT"],
#         ["DOT", "USDT"]]

# for i in pairs:
#     print(i, get_price("".join(i)))