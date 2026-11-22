def place_order(client, symbol, side, order_type, quantity, price=None):
    if order_type.upper() == "MARKET":
        return client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type='MARKET',
            quantity=quantity
        )
    elif order_type.upper() == "LIMIT":
        return client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type='LIMIT',
            quantity=quantity,
            price=price,
            timeInForce='GTC' # GTC means "Good 'Till Cancelled"
        )