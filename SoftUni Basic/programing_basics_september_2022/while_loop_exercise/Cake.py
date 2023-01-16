width = int(input())
length = int(input())
cake = width * length
sum_peaces = 0

peace_of_cake = input()
while peace_of_cake != "STOP":
    a = int(peace_of_cake)
    sum_peaces = sum_peaces + a
    if cake < sum_peaces:
        break
    peace_of_cake = input()

delta = abs(cake - sum_peaces)
if sum_peaces > cake:
    print(f"No more cake left! You need {delta} pieces more.")
else:
    print(f"{delta} pieces are left.")
