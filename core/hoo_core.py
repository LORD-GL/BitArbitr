# import requests
# import json
# import hmac

# api_key = "sjFWgTBLamXRf2H7DJQbxn4HLGNYdX"
# secret = "ZBjufrMoew3eH2BC9ftkSAJNgFWEbRx7uXNpYHATxMgnDzb6aG"
# code = "btcusdt"
# resp = requests.get(f"https://api.hoolgd.com/pairs/{code}/ticker?client_id={api_key}&client_key={secret}")
# print(resp)

# sign = hmac.New(client_key, sign_str, sha256)
# https://github.com/chaince/apidocs/blob/master/restful-pairs.md#get-ticker
# https://hoo.com/docs-en/#connection-guide