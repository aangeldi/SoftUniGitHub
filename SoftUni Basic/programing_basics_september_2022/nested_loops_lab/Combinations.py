num = int(input())
counter = 0
sum = 0
for i in range(0, num + 1):
    for j in range(0, num + 1):
        for k in range(0, num + 1):
            sum = i + j + k
            if sum == num:
                counter = counter + 1
print(f"{counter}")