import requests
import json 
# tBTCUSDT

def get_price(base, quor):
    if quor == "USDC":
        return -1
    #pair[1] = pair[1][:-1]
    quor = quor[:-1]
    #symbol = "".join(pair)
    resp = requests.get(f"https://api-pub.bitfinex.com/v2/ticker/t{base+quor}", verify=False).json()
    if resp[0] != 'error':
        return float(resp[0])
    else:
        return -1