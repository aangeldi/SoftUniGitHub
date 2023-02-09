numbers = input().split(", ")  # 1, 2, 3, 4, 5
beggars = int(input())  # 2
beggars_collection = [0] * beggars
temp = 0

for i in range(len(numbers)):
    temp = i % beggars
    beggars_collection[temp] += int(numbers[i])

print(beggars_collection)

