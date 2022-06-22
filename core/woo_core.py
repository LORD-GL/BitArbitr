# https://api.woo.org/ /v1/public/info
import requests
import json

list_woo = []
resp_w = requests.get("https://api.woo.org/v1/public/info").json()['rows']
for i in resp_w:
    list_woo.append(i['symbol'])


# Content-Type: application/x-www-form-urlencoded
# x-api-key: AbmyVJGUpN064ks5ELjLfA==
# x-api-signature: 20da0852f73b20da0208c7e627975a59ff072379883d8457d03104651032033d

def get_price(symbol="SPOT_BTC_USDT"):
    if symbol not in list_woo:
        return -1, -1
    resp = requests.get("https://api.woo.org/v1/kline", header=header).json()
    print(resp)

    