# simple-display-of-crypto-through-api

A tiny terminal dashboard that shows live crypto prices from Binance's public API, refreshed every second, right in your terminal.

## What it does

`K.py` pulls 24hr ticker data for a fixed list of coins from Binance and renders it as a live-updating table using [Rich](https://github.com/Textualize/rich). No API key needed — it's Binance's public market data endpoint.

Tracked symbols (edit `SYMBOLS` in `K.py` to change):
- BTC
- ETH
- SOL
- XRP
- DOGE

For each coin it shows:
- Current price (USDT)
- 24h % change (green if up, red if down)

## Requirements

- Python 3.8+
- `requests`
- `rich`

## Setup

```bash
git clone https://github.com/Glory-bot-art/simple-display-of-crypto-through-api.git
cd simple-display-of-crypto-through-api
pip install requests rich
```

## Usage

```bash
python K.py
```

Press `Ctrl+C` to stop.

## Notes

- No API key required — this only calls Binance's public `/api/v3/ticker/24hr` endpoint.
- If the request fails (network issue, rate limit, etc.), the table shows an `Error` row instead of crashing.
- Refreshes once per second.

