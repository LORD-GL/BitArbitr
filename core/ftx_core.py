import json
import requests
from dotenv import load_dotenv
load_dotenv()

def get_price(base_cur='BTC', quote_cur='USDT'):
<<<<<<< HEAD
    if base_cur == 'RUNE' and quote_cur == "USDT":
        return -1, -1
    endpoint = "https://ftx.com/api/markets"
    request_url = f"{endpoint}/{base_cur}/{quote_cur}" #BTC/USDT
    try:
        ans = requests.get(request_url).json()
    except:
        return -1, -1
    if ans['success'] == True:
        return float(ans['result']['price']), round( float(ans['result']['volumeUsd24h']) / float(ans['result']['price']), 2)
    else:
        return -1, -1
=======
    if quote_cur == 'USDC':
        return -1, -1
    endpoint = "https://ftx.com/api/markets"
    request_url = f"{endpoint}/{base_cur}/{quote_cur}" #BTC/USDT
    ans = requests.get(request_url).json()
    if ans['success'] == True:
        return float(ans['result']['price']), round( float(ans['result']['volumeUsd24h']) / float(ans['result']['price']), 2)
    else:
        return -1, -1
>>>>>>> 0b8050ac48e11cc04560f6d039510486349dd868
