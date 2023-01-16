num = int(input())
current = 1
flag = 0
for i in range(1, num + 1):
    for col in range(1, i + 1):
        if current > num:
            flag = 1
            break
        print(str(current) + ' ', end='')
        current = current + 1
    if flag:
        break
    print()