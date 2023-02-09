items = input().split("|")
budget = int(input())
bought = []
total_profit = []
profit = 0
expenses_flag = 0
flag = 0
counter = 1

for item in range(len(items)):
    new_item = items[flag].split("->")
    clothes = new_item[0]
    price = float(new_item[1])
    flag += 1
    if clothes == "Clothes" and price > 50.00:
        continue
    elif clothes == "Shoes" and price > 35.00:
        continue
    elif clothes == "Accessories" and price > 20.50:
        continue
    if budget >= price:
        percent = price * 0.4
        profit = price + percent
        if expenses_flag == 0:
            total_profit.append(float(percent))
            bought.append(float(profit))
        budget = budget - price
        counter += 1
    else:
        expenses_flag = 1
        budget = budget + sum(bought) - price
        flag -= 1

for prof in bought:
    print(f"{prof:.2f}", end=" ")
print("")
suma = sum(total_profit)
print(f"{suma:.2f}")

if counter < len(items):
    print("Not enough money.")
else:
    print("Hello, France!")
