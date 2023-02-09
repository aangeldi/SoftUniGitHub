event = input().split("|")
energy = 100
initial_coins = 100
# current_energy = 0
# current_coins = 0
# gained_energy = 0
day = 0
name = ""
temp = energy
for ev in event:
    elements = ev.split("-")
    name = elements[0]
    gained_energy = int(elements[1])

    if name == "rest":
        if temp < energy + gained_energy:
            gained_energy = gained_energy - gained_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
        else:
            energy = energy + gained_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
    elif name == "order":
        initial_coins = initial_coins + gained_energy
        energy -= 30
        if energy >= 0:
            print(f"You earned {gained_energy} coins.")
        else:
            energy += 50
            day = 1
            break
    else:
        # initial_coins = initial_coins - gained_energy
        if initial_coins - gained_energy < 0:
            day = 1
            break
        else:
            initial_coins = initial_coins - gained_energy
            print(f"You bought {name}.")

if day == 0:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {energy}")
else:
    print(f"You had to rest!")
    print(f"Closed! Cannot afford {name}.")
