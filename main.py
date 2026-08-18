import requests

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raise exception for HTTP errors

    data = response.json()
    price = float(data["price"])
    print(f"BTC/USDT: ${price:,.2f}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching price: {e}")
# 24 hours change
