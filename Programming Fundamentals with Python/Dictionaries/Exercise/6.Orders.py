products = input()
products_dictionary = {}

while products != "buy":
    products = products.split()
    name = products[0]
    price = float(products[1])
    quantity = int(products[2])
    if name not in products_dictionary:
        products_dictionary[name] = {}
        products_dictionary[name]["price"] = price
        products_dictionary[name]["quantity"] = quantity
    else:
        products_dictionary[name]["price"] = price
        products_dictionary[name]["quantity"] += quantity

    products = input()

for key, value in products_dictionary.items():
    total_price = value['price'] * value["quantity"]
    print(f"{key} -> {total_price:.2f}")

