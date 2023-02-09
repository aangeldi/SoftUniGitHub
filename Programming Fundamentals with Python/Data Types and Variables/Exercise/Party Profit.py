group_size = int(input())
days = int(input())
spend = 0
earn = 0
total = 0
for i in range(1, days + 1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5
        spend += 2 * group_size

    earn += 50
    spend += 2 * group_size
    if i % 3 == 0:
        spend += 3 * group_size
    if i % 5 == 0:
        earn += 20 * group_size

total = (earn - spend) // group_size
print(f"{group_size} companions received {total} coins each.")


