import json
import time

import requests
from rich.live import Live
from rich.table import Table

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT"]
BINANCE_URL = "https://api.binance.com/api/v3/ticker/24hr"


def fetch_table_data() -> Table:
    """Fetch ticker data from Binance and build a fresh Rich Table."""
    table = Table(title="Live Binance Prices (Ctrl+C to stop)")
    table.add_column("Coin", style="cyan", no_wrap=True)
    table.add_column("Price", style="green", justify="right")
    table.add_column("24h Change", justify="right")

    try:
        response = requests.get(
            BINANCE_URL,
            params={"symbols": json.dumps(SYMBOLS, separators=(",", ":"))},
            timeout=3,
        )
        data = response.json()

        for item in data:
            symbol = item["symbol"].replace("USDT", "")
            price = float(item["lastPrice"])
            change = float(item["priceChangePercent"])

            # Colorize positive and negative 24h changes
            change_color = "green" if change >= 0 else "red"
            change_str = f"[{change_color}]{change:+.2f}%[/{change_color}]"

            table.add_row(symbol, f"${price:,.4f}", change_str)

    except requests.RequestException as e:
        table.add_row("Error", str(e), "-")

    return table


if __name__ == "__main__":
    try:
        with Live(fetch_table_data(), refresh_per_second=1) as live:
            while True:
                time.sleep(1)
                live.update(fetch_table_data())
    except KeyboardInterrupt:
        print("\nprogram stopped.")