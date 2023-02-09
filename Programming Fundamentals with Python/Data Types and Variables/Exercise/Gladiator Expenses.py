lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet = 0
sward = 0
shield = 0
armor = 0

for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        helmet += 1
    if i % 3 == 0:
        sward += 1
    if i % 6 == 0:
        shield += 1
    if i % 12 == 0:
        armor += 1

expenses = helmet * helmet_price + sword_price * sward + shield_price * shield + armor_price * armor
print(f"Gladiator expenses: {expenses:.2f} aureus")