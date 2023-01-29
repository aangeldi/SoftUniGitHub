array = [23, 12, 334, 1000, 3, 2, 111,2]
temp = 0

for i in range(len(array)):
    for j in range(len(array) - 1):
        if array[j] < array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            # temp = array[j]
            # array[j] = array[j + 1]
            # array[j + 1] = temp

print(array)

a = 239

b = a % 10
print(b)
b = a // 10
print(b)
