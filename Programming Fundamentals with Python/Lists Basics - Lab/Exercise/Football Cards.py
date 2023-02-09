# A-1 A-5 A-10 B-2
red_cards = input().split()
count_a = 0
count_b = 0
first_team = []
second_team = []
# print(red_cards)
flag = 0
for card in red_cards:
    if card in first_team or card in second_team:
        continue
    cards = card.split("-")
    team = cards[0]
    num = cards[1]

    if team == "A":
        first_team.append(card)
        count_a += 1
    else:
        second_team.append(card)
        count_b += 1
    if count_b > 4 or count_a > 4:
        flag = 1
        break
    else:
        pass

if flag == 1:
    print(f"Team A - {11 - count_a}; Team B - {11 - count_b}")
    print("Game was terminated")
else:
    print(f"Team A - {11 - count_a}; Team B - {11 - count_b}")
