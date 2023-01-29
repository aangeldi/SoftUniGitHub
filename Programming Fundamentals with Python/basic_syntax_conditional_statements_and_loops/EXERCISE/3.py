text = input()

my_list = text.split(" ")
new_list = [int(x) for x in  my_list]

for i in range(len(new_list)):
    new_list[i] = -new_list[i]

print(new_list)