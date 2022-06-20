import json
import requests
from dotenv import load_dotenv
load_dotenv()

def get_price(base_cur='BTC', quote_cur='USDT'):
    if quote_cur == 'USDC':
        return -1, -1
    endpoint = "https://ftx.com/api/markets"
    request_url = f"{endpoint}/{base_cur}/{quote_cur}" #BTC/USDT
    ans = requests.get(request_url).json()
    if ans['success'] == True:
        return float(ans['result']['price']), round( float(ans['result']['volumeUsd24h']) / float(ans['result']['price']), 2)
    else:
        return -1, -1
