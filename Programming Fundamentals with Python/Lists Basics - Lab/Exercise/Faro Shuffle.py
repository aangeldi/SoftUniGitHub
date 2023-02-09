cards = input().split()
shuffles_count = int(input())

for j in range(shuffles_count):
    first_faro = []
    second_faro = []
    for i in range(1, len(cards) - 1):
        if i < len(cards) / 2:
            first_faro.append(cards[i])
        else:
            second_faro.append(cards[i])

    shuffled = []
    first_part_idx = 0
    second_part_idx = 0
    for idx in range(len(first_faro) * 2):
        if idx % 2 == 0:
            shuffled.append(second_faro[second_part_idx])
            second_part_idx += 1
        else:
            shuffled.append(first_faro[first_part_idx])
            first_part_idx += 1

    cards = [cards[0]] + shuffled + [cards[-1]]
print(cards)
