n = int(input())
lenght = int(input())
my_list = []
index = 1

while True:
    if index % n == 0:
        my_list.append(index)
    if len(my_list) == lenght:
        break
    index += 1

print(my_list)
