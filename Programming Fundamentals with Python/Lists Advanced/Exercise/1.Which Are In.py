first_string = input().split(", ")
second_string = input().split(", ")
new_string = []

for el in first_string:
    for idx in range(len(second_string)):
        if el in second_string[idx]:
            new_string.append(el)
            break
print(new_string)