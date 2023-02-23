items = input().split("|")
budget = int(input())
bought_amount = 0
not_enough_money = 0
profit = 0

for item in range(len(items)):
    new_item = items[item].split("->")
    clothes = new_item[0]
    price = float(new_item[1])

    if budget < price:
        not_enough_money += price
        continue

    if clothes == "Clothes":
        if price > 50.00:
            continue
        budget -= price
        profit += price * 0.4
        bought = price + price * 0.4
        print(f"{bought:.2f}", end=" ")
    if clothes == "Shoes":
        if price > 35.00:
            continue
        budget -= price
        profit += price * 0.4
        bought = price + price * 0.4
        print(f"{bought:.2f}", end=" ")
    if clothes == "Accessories":
        if price > 20.50:
            continue
        budget -= price
        profit += price * 0.4
        bought = price + price * 0.4
        print(f"{bought:.2f}", end=" ")

print("")
print(f"Profit: {profit:.2f}")
if (budget + profit) < not_enough_money:
    print("Not enough money.")
else:
    print("Hello, France!")
