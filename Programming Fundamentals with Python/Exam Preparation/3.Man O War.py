pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]
maximum_health_capacity = int(input())


def is_valid_idx(indexation, seq):
    return 0 <= indexation < len(seq)


is_index = True
while is_index:
    line = input()
    if line == "Retire":
        break
    command_args = line.split()
    command = command_args[0]

    if command == "Fire":
        idx = int(command_args[1])
        damage = int(command_args[2])
        if not is_valid_idx(idx, war_ship):
            continue
        war_ship[idx] -= damage
        if war_ship[idx] <= 0:
            print("You won! The enemy ship has sunken.")
            is_index = False
    elif command == "Defend":
        startIndex = int(command_args[1])
        endIndex = int(command_args[2])
        damage = int(command_args[3])
        if not is_valid_idx(startIndex, pirate_ship) or not is_valid_idx(endIndex, pirate_ship):
            continue
        for section in range(startIndex, endIndex + 1):
            pirate_ship[section] -= damage
            if pirate_ship[section] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_index = False
                break
    elif command == "Repair":
        index = int(command_args[1])
        health = int(command_args[2])
        if not is_valid_idx(index, pirate_ship):
            continue
        pirate_ship[index] = min(maximum_health_capacity, pirate_ship[index] + health)
    elif command == "Status":
        threshold = maximum_health_capacity * 0.2
        counter = 0
        for section in pirate_ship:
            if section < threshold:
                counter += 1
        print(f"{counter} sections need repair.")

if is_index:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
