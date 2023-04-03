first, second = input().split()
sum = 0
delta = abs(len(first) - len(second))
first_array = []
second_array = []
for i in range(len(first)):
    first_array.append(ord(first[i]))
for i in range(len(second)):
    second_array.append(ord(second[i]))

if len(first) > len(second):
    for i in range(delta):
        second_array.append(1)
elif len(first) < len(second):
    for i in range(delta):
        first_array.append(1)

for i in range(len(first_array)):
    sum += first_array[i] * second_array[i]

print(sum)

