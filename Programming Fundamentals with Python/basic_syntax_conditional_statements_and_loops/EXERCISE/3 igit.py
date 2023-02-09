array = [222, 32, 45, 1, 26, 22, -32, -212, -22]
array_str = str(array)
print(array_str)
length = len(array)
flag = 0
counter = 0
a = 1
for i in range(length):
    if 99 < abs(array[i]) < 1000:
        temp = abs(array[i]) % 10
        if temp == 2:
            counter = counter + 1
        flag = abs(array[i]) // 10
        temp = flag % 10
        if temp == 2:
            counter = counter + 1
        temp = flag // 10
        if temp == 2:
            counter = counter + 1
    else:
        continue
print(counter)

txt = "234"
for i in range(len(txt)):
    print(txt[i])