data = [i for i in input().lower().split()]

programming_languages = dict.fromkeys(data, 0)

for word in data:
    if word in programming_languages.keys():
        programming_languages[word] += 1

for key, value in programming_languages.items():
    if value % 2 != 0:
        print(f"{key}", end=" ")

