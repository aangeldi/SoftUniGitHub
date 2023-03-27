stock = input().split()
search_products = input().split()
products = {}
for idx in range(0, len(stock), 2):
    products[stock[idx]] = int(stock[idx + 1])

for product in search_products:
    if product in products.keys():
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


