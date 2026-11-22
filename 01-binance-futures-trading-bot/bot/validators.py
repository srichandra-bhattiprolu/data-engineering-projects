def validate_order_input(quantity, price, order_type):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    
    if order_type.upper() == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Limit orders require a price greater than zero.")