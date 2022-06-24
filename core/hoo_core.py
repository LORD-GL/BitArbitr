import requests
import json

pairs_hoo = []
resp_hoo = requests.get("https://api.hoolgd.com/open/v1/tickers/market").json()['data']
for i in resp_hoo:
    pairs_hoo.append(i['symbol'])

def get_price(symbol="BTC-USDT"):
    if symbol not in pairs_hoo:
        return -1, -1
    elif "NFT" in symbol or "GMT" in symbol or "XCH" in symbol: return -1, -1
    resp = requests.get(f"https://api.hoolgd.com/open/v1/tickers/market?symbol={symbol}").json()['data'][0]
    return float(resp['price']), round(float(resp['volume']), 2)