def is_card_in_deck(arg):
    if arg not in cards:
        return True
    return False


def is_index_in_range(idx):
    return 0 <= idx < len(cards)


cards = input().split(", ")

n = int(input())

for i in range(n):
    command_args = input().split(", ")
    command = command_args[0]
    card = command_args[1]

    if command == "Add":
        if not is_card_in_deck(card):
            print("Card is already in the deck")
        else:
            cards.append(card)
            print("Card successfully added")
    elif command == "Remove":
        if is_card_in_deck(card):
            print("Card not found")
        else:
            cards.remove(card)
            print("Card successfully removed")
    elif command == "Remove At":
        index = int(command_args[1])
        if not is_index_in_range(index):
            print("Index out of range")
        else:
            cards.pop(index)
            print("Card successfully removed")
    elif command == "Insert":
        index = int(command_args[1])
        card_name = command_args[2]
        if not is_index_in_range(index):
            print("Index out of range")
        elif not is_card_in_deck(card_name):
            print("Card is already added")
        else:
            cards.insert(index, card_name)
            print("Card successfully added")

print(", ".join(cards))
