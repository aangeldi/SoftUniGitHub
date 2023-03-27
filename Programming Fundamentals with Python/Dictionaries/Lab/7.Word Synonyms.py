num = int(input())

synonyms = {}

for _ in range(num):
    word = input()
    synonym = input()

    if word not in synonyms.keys():
        synonyms[word] = []
    synonyms[word].append(synonym)


for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")

