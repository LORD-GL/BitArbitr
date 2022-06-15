import json
import requests
from dotenv import load_dotenv
load_dotenv()

def get_price(base_cur='BTC', quote_cur='USDT'):
    endpoint = "https://ftx.com/api/markets"
    request_url = f"{endpoint}/{base_cur}/{quote_cur}" #BTC/USDT
    ans = requests.get(request_url, verify=False).json()
    if ans['success'] == True:
        return float(requests.get(request_url).json()['result']['price'])
    else:
        return -1