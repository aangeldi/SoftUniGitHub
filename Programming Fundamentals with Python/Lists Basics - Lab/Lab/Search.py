n = int(input())
word = input()

positive = []
new_list = []
for _ in range(n):
    string = str(input())
    positive.append(string)
print(positive)
for i in range(len(positive)):
    if word in positive[i]:
        new_list.append(positive[i])
print(new_list)
