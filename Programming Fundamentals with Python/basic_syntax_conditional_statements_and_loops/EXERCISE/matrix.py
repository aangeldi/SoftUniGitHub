M1 = [[8, 14, -6],
      [12, 7, 4],
      [-11, 3, 21]]

M2 = [[3, 16, -6],
      [9, 7, -4],
      [-1, 3, 13]]

M3 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

# sum below/above the left diagonal
sum = 0
for i in range(len(M1)):
    for j in range(len(M1)):
        if i > j:
            sum = sum + M1[i][j]
print(sum)

# sum left diagonal M1
sum = 0
for i in range(len(M1)):
    for j in range(len(M1)):
        if i == j:
            sum = sum + M1[i][j]
print(sum)

# sum right diagonal M1
length = len(M1)
sum = 0
counter = 0
for i in range(length):
    for j in range(length - 1, -1, -1):
        if i == counter:
            sum = sum + M1[i][-1 + (-i)]
            counter += 1
print(sum)

# sum of Matrices
for i in range(len(M1)):
    for k in range(len(M2)):
        M3[i][k] = M1[i][k] + M2[i][k]
print(M3)
