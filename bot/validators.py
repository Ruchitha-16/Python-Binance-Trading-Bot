def validate_side(side):

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type):

    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP")


def validate_quantity(quantity):

    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError("Quantity must be greater than zero")
    except:
        raise ValueError("Quantity must be a valid number")


def validate_price(price):

    if price is None:
        return

    try:
        p = float(price)
        if p <= 0:
            raise ValueError("Price must be greater than zero")
    except:
        raise ValueError("Price must be a valid number")