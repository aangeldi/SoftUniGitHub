stock = input()

products = {}

while stock != "statistics":
    stock = stock.split(": ")
    product = stock[0]
    quantity = int(stock[1])
    if product not in products.keys():
        products[product] = quantity
    else:
        products[product] += quantity

    stock = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
