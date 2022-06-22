import requests
import json

#https://api.aex.zone /v3/ticker.php?coinname=btc&mk_type=usdt

pairs_aex = []
resp_aex = requests.get("https://api.aex.zone/v3/allpair.php").json()['data']

for i in resp_aex:
    pairs_aex.append([i['coin'], i['market']])


def get_price(base="btc", quor="usdt"):
    if [base, quor] not in pairs_aex:
        return -1, -1
    resp = requests.get(f"https://api.aex.zone/v3/ticker.php?coinname={base}&mk_type={quor}").json()['data']['ticker']
    return float(resp['last']), round(float(resp['vol']), 2)
