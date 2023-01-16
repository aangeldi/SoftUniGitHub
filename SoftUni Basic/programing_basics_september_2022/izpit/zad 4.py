number = int(input())
rate = 0
sales = 0
sum_sold = 0
sum_rate = 0
for i in range(1, number + 1):
    sales = int(input())
    rate = sales % 10
    sold = sales // 10
    if rate == 2:
        sold = sold * 0
    elif rate == 3:
        sold = sold * 0.50
    elif rate == 4:
        sold = sold * 0.70
    elif rate == 5:
        sold = sold * 0.85
    elif rate == 6:
        sold = sold * 1.00
    sum_sold = sum_sold + sold
    sum_rate = (sum_rate + rate)
sum_rate = sum_rate/number
print(f"{sum_sold:.2f}")
print(f"{sum_rate:.2f}")