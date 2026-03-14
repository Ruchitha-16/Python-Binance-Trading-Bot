import logging


def place_order(client, symbol, side, order_type, quantity, price=None):

    order = None

    try:

        if order_type == "MARKET":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Unsupported order type")

        logging.info(f"Order placed: {order}")

        return order

    except Exception as error:

        logging.error(f"Order failed: {error}")

        raise