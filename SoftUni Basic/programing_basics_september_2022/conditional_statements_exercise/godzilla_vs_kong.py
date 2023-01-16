budget = float(input())
statists = int(input())
suit_price = float(input())
decor = budget*0.1

if statists > 150:
    discount = suit_price*0.1
    suit_price = suit_price - discount

money_for_suits = statists * suit_price

if ((decor + money_for_suits) > budget):
    delta = ((decor + money_for_suits) - budget)
    print("Not enough money!")
    print(f"Wingard needs {delta:.2f} leva more.")
else:
    left_money = (budget - (decor + money_for_suits))
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")