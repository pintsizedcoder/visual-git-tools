def calculate_total(price, quantity):
    total = price * quantity
    return round(total, 2)


print(f"Checkout total: ${calculate_total(11, 3): .2f}")