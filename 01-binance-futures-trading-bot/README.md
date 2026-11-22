# Binance Futures Trading Bot (Testnet)

A Python command-line tool that places **market** and **limit** orders on the **Binance Futures Testnet** through the Binance REST API. It checks inputs before sending an order and logs every API call to a file.

> ⚠️ Runs on the **testnet only** (`testnet=True`). No real money is used.

## Features

- Market and limit orders (limit orders use Good-Till-Cancelled)
- Input validation: quantity must be above zero, and limit orders must have a price
- Logging to both the terminal and `trading_bot.log`
- API keys loaded from a `.env` file, never hard-coded
- Clean, modular code: the client, orders, validation and logging each live in their own module

## Tech

Python · python-binance · python-dotenv · argparse · logging

## Project structure

```
├── cli.py              # Entry point: reads command-line arguments and runs the order flow
├── bot/
│   ├── client.py       # Connects to the Binance Futures Testnet
│   ├── orders.py       # Places market / limit orders
│   ├── validators.py   # Checks inputs before sending
│   └── logging_config.py
├── requirements.txt
└── .env.example        # Template for your API keys
```

## Setup

Run these commands from inside this folder (`01-binance-futures-trading-bot/`).

```bash
python -m venv venv
# Windows: .\venv\Scripts\activate    macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # then add your Binance Testnet API key and secret
```

## Usage

```bash
# Market order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

# Limit order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

## Sample log output

```
2026-04-22 16:56:11,543 - INFO - Attempting to place MARKET BUY order for BTCUSDT
2026-04-22 16:56:12,371 - INFO - SUCCESS: Order 13061161302 placed.
2026-04-22 19:25:44,657 - INFO - Attempting to place LIMIT BUY order for BTCUSDT
2026-04-22 19:25:45,748 - INFO - SUCCESS: Order 13061542861 placed.
```
