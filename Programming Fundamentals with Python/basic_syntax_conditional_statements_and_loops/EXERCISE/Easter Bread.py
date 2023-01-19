import math

budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price + flour_price * 0.25
loaf_price = 0.25 * milk_price + flour_price + eggs_price
loafs = math.floor(budget/(0.25 * milk_price + flour_price + eggs_price))
rest = budget - (loafs * loaf_price)
eggs = 0

for i in range(1, loafs + 1):
    eggs += 3
    if i % 3 == 0:
        eggs = eggs - (i - 2)
print(f"You made {loafs} loaves of Easter bread! Now you have {eggs} eggs and {rest :.2f}BGN left.")





