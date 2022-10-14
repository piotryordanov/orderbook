import json
import requests

coinbase_url = "https://api.pro.coinbase.com/products/BTC-USD/book?level=2"
gemini_url = "https://api.gemini.com/v1/book/BTCUSD"
def fetch_books(exchange):
    if exchange == "coinbase":
        url = coinbase_url
    else:
        url = gemini_url

    response = requests.get(url)
    json_response = response.json()
    return json_response
