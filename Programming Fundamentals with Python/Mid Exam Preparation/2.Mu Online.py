health = 100
bitcoins = 0
total_health = health
rooms = input().split("|")
is_alive = True
for i in range(len(rooms)):
    # commmand_args =
    command = rooms[i].split()[0]
    number = int(rooms[i].split()[1])

    if command == "potion":
        total_health = total_health + number
        if health < total_health:
            var = number - (total_health - health)
            total_health = health
            print(f"You healed for {var} hp.")
        else:
            print(f"You healed for {number} hp.")

        print(f"Current health: {total_health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        total_health -= number
        if total_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i + 1}")
            is_alive = False
            break
if is_alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {total_health}")