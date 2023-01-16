word = str(input())
reverse = ""

for i in range(len(word) -1, -1, -1):
    reverse = reverse + word[i]
print(f"{reverse}")
