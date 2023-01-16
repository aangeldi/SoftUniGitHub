budget = float(input())
season = str(input())
persons = int(input())
price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if persons <= 6:
    price = price * 0.90
elif 6 < persons <= 11:
    price = price * 0.85
elif persons > 11:
    price = price * 0.75

if persons % 2 == 0 and season != "Autumn":
    price = price * 0.95

dif = abs(price - budget)
if budget >= price:
    print(f"Yes! You have {dif:.2f} leva left.")
else:
    print(f"Not enough money! You need {dif:.2f} leva.")
