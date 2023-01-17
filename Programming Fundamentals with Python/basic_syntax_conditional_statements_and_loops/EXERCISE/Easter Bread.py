import math

budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price + flour_price * 0.25
loaf_price = 0.25 * milk_price + flour_price + eggs_price
loafs = math.floor(budget/(0.25 * milk_price + flour_price + eggs_price))
rest = budget - (loafs * loaf_price)
refer = loafs // 3
colored_eggs = refer * loafs - (refer - 2)

print(colored_eggs)

for i in range(loafs):
    if i % 3 == 0:


