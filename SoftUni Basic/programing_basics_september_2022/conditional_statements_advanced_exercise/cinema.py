screening_type = str(input())
rows = int(input())
columns = int(input())
total = 0
premiere_price = 12.00
normal_price = 7.50
discount_price = 5.00

if screening_type == "Premiere":
    total = premiere_price * rows * columns
elif screening_type == "Normal":
    total = normal_price * rows * columns
elif screening_type == "Discount":
    total = discount_price * rows * columns

print(f"{total:.2f} leva")
