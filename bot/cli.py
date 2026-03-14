import argparse

from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logging


API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"


def main():

    setup_logging()

    parser = argparse.ArgumentParser(description="Simple Binance Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (example: BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET / LIMIT / STOP")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Price required for LIMIT and STOP orders")

    args = parser.parse_args()

    # Validate inputs
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)
    validate_price(args.price)

    # Create Binance client
    client = BinanceClient(API_KEY, API_SECRET).get_client()

    # Place order
    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    # Print clean output
    print("\nOrder Request Summary")
    print("----------------------")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    print(f"Price: {args.price}")

    print("\nOrder Response")
    print("----------------------")
    print(f"Order ID: {order.get('orderId')}")
    print(f"Status: {order.get('status')}")
    print(f"Executed Quantity: {order.get('executedQty')}")
    print(f"Average Price: {order.get('avgPrice')}")


if __name__ == "__main__":
    main()