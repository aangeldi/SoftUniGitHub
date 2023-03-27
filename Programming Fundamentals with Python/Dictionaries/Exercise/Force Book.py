side_by_player = {}
players_by_side = {}

while True:
    line = input()
    if line == 'Lumpawaroo':
        break

    if " | " in line:
        command_args = line.split(' | ')
        force_side = command_args[0]
        force_user = command_args[1]

        if force_side not in players_by_side:
            players_by_side[force_side] = []

        if force_user not in side_by_player:
            side_by_player[force_user] = force_side
            players_by_side[force_side].append(force_user)
    else:
        command_args = line.split(' -> ')
        force_user = command_args[0]
        force_side = command_args[1]

        if force_side not in players_by_side:
            players_by_side[force_side] = []

        players_by_side[force_side].append(force_user)

        if force_user in side_by_player:
            old_side = side_by_player[force_user]
            players_by_side[old_side].remove(force_user)
            side_by_player[force_user] = force_side
        else:
            side_by_player[force_user] = force_side

        print(f'{force_user} joins the {force_side} side!')

for side, members in players_by_side.items():
    if len(members) == 0:
        continue

    print(f'Side: {side}, Members: {len(members)}')
    for member in members:
        print(f'! {member}')