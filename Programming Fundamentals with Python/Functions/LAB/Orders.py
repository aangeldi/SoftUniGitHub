def total_price(product, quantity):
    total = None
    if product == "coffee":
        total = quantity * 1.5
    elif product == "coke":
        total = quantity * 1.4
    elif product == "water":
        total = quantity * 1.0
    elif product == "snacks":
        total = quantity * 2.0
    return f"{total:.2f}"


product_arg = input()
quantity_arg = int(input())

print(total_price(product_arg, quantity_arg))
