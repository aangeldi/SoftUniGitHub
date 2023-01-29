elements = input().split()

new_list = []

for el in range(len(elements)):
    num = int(elements[el])
    new_list.append(-num)

print(new_list)