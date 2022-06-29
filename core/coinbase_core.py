import cbpro
client = cbpro.PublicClient( #AuthenticatedClient
    # "7sqshueErharJjBM",
    # "WeWBTRaKoFMPLV9wD0QqgJrricQuWbxd"
)

#print(client.get_product_ticker('BTC-USDT')['price'])

def get_price(symbol="BTC-USDT"):
    try:
        data = client.get_product_ticker(symbol)
    except:
        return -1, -1
    try:
        # print(data)
        return float(data['price']), round( float(data['volume']), 2)
    except:
        return -1, -1

# get_price()