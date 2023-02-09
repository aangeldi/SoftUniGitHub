numbers = str(input())
a = numbers.split()
new_list = []

for i in range(len(a)):
    b = (int(a[i]))
    new_list.append(-b)
print(new_list)
