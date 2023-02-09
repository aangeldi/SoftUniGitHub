n = int(input())
new_list = []
collected = []
for _ in range(n):
    numbers = int(input())
    new_list.append(numbers)
command = input()

if command == "even":
    for i in range(len(new_list)):
        if new_list[i] % 2 == 0 or new_list[i] == 0:
            collected.append(new_list[i])
elif command == "odd":
    for i in range(len(new_list)):
        if new_list[i] % 2 != 0:
            collected.append(new_list[i])
elif command == "negative":
    for i in range(len(new_list)):
        if new_list[i] < 0:
            collected.append(new_list[i])
elif command == "positive":
    for i in range(len(new_list)):
        if new_list[i] >= 0:
            collected.append(new_list[i])

print(collected)
