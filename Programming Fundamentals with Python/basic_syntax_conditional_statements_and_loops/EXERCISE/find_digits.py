array = [222, 32, 45, 1, 26, 22, -32, -222, -22]
length = len(array)
counter = 0
a = 1
for i in range(length):
    if 99 < abs(array[i]) < 1000:
        while a != 0:
            temp = abs(array[i]) % 10
            if temp == 2:
                counter = counter + 1
                temp = abs(array[i]) // 10
            if temp == 2:
                counter = counter + 1
            a = (abs(array[i]) % 10) // 10
    else:
        continue
print(counter)
