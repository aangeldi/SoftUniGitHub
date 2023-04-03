word = input().split()

for i in range(len(word)):
    word[i] = word[i] * len(word[i])

concatenated = "".join(word)
print(concatenated)