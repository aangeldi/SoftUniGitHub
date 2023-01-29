masiv = [222, 32, 45, 1, 26, 22, -32, -222, -22]
legth = len(masiv)
counter = 0

for i in range(legth):
    if 9 < abs(masiv[i]) < 100:
        temp = abs(masiv[i]) % 10
        if temp == 2:
            counter = counter + 1

        temp = abs(masiv[i]) // 10
        if temp == 2:
            counter = counter + 1
    else:
        continue
print(counter)
