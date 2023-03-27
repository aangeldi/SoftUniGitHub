data = input().split()
words = {}

for el in data:
    for index in range(len(el)):
        if el[index] not in words:
            words[el[index]] = 1
        else:
            words[el[index]] += 1

for key, value in words.items():
    print(f"{key} -> {value}")