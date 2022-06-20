from poloniex import Poloniex
polo = Poloniex()
def get_price(base="BTC", quor="USDT"):
    #symbol="USDT_BTC"):
    try:
        ticker = polo.returnTicker()[quor + "_" + base]
    except:
        return -1, -1
    #print(ticker['quoteVolume'])
    return float(ticker['last'])

