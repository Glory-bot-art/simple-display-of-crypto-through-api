import json
import requests

# List of Binance trading pairs
symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT"]

# Make 1 single API call for all 5 coins
url = "https://api.binance.com/api/v3/ticker/24hr"
response = requests.get(url, params={"symbols": json.dumps(symbols, separators=(",", ":"))})
data = response.json()

print(f"{'Coin':<10} {'Price':<14} {'24h Change':<10}")
print("-" * 36)

for item in data:
    symbol = item["symbol"].replace("USDT", "")
    price = float(item["lastPrice"])
    change = float(item["priceChangePercent"])

    print(f"{symbol:<10} ${price:<13,.4f} {change:+.2f}%")

