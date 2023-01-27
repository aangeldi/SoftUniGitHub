quantity_decoration = int(input())
days_left_until_christmas = int(input())
price = 0
points = 0

for i in range(1, days_left_until_christmas + 1):
    if i % 2 == 0:
        price += 2 * quantity_decoration
        points += 5
    if i % 3 == 0:
        price += 8 * quantity_decoration
        points += 13
    if i % 5 == 0:
        price += 15 * quantity_decoration
        points += 17
    if i % 15 == 0:
        points += 30
    if i % 11 == 0:
        quantity_decoration += 2
    if i % 10 == 0:
        price += 23
        points -= 20
    if i % 10 == 0 and i == days_left_until_christmas:
        points -= 30
print(f"Total cost: {price}")
print(f"Total spirit: {points}")
