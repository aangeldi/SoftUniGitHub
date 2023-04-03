tickets = [i.strip() for i in input().split(", ")]
first_part = ""
second_part = ""
win_symbols = ['@', '#', '$', '^']
sym = ""
for ticket in tickets:
    counter_first = 0
    counter_second = 0
    flag = False
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    first_part = ticket[:10]
    second_part = ticket[10:]

    for symbol in win_symbols:
        if symbol in first_part and symbol in second_part:
            sym = symbol
            idx_first = first_part.index(sym)
            idx_second = second_part.index(sym)
            for idx_first in range(idx_first, len(first_part)):
                if first_part[idx_first] == sym:
                    counter_first += 1
                else:
                    break
            for idx_second in range(idx_second, len(second_part)):
                if second_part[idx_second] == sym:
                    counter_second += 1
                else:
                    break
    counter = min(counter_first, counter_second)

    if counter == 10:
        print(f'ticket "{first_part + second_part}" - {counter}{sym} Jackpot!')
    elif counter >= 6:
        print(f'ticket "{first_part + second_part}" - {counter}{sym}')
    else:
        print(f'ticket "{first_part + second_part}" - no match')
