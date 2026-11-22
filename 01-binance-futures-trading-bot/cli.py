import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import argparse
import logging
from bot.client import get_binance_client
from bot.orders import place_order
from bot.logging_config import setup_logging
from bot.validators import validate_order_input

# Start the logger
logger = setup_logging()

def main():
    # 1. Setup the "Command Line" instructions
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", type=str, required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    # 2. Validation: If it's a LIMIT order, we MUST have a price
    if args.type == "LIMIT" and not args.price:
        print("Error: Limit orders require a --price")
        return

    try:
        # 3. Connect to Binance
        logger.info(f"Attempting to place {args.type} {args.side} order for {args.symbol}")
        client = get_binance_client()

        validate_order_input(args.quantity, args.price, args.type)
        
        # 4. Place the order
        response = place_order(
            client, 
            args.symbol, 
            args.side, 
            args.type, 
            args.quantity, 
            args.price
        )

        # 5. Print Success Message
        print("\n✅ Order Placed Successfully!")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Avg Price: {response.get('avgPrice')}")
        
        logger.info(f"SUCCESS: Order {response.get('orderId')} placed.")

    except Exception as e:
        print(f"API Error: {e}")
        logger.error(f"FAILED: {e}")

if __name__ == "__main__":
    main()