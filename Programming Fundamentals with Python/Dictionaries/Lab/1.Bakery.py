data = input().split()
stock = {}

for i in range(0, len(data), 2):
    stock[data[i]] = int(data[i + 1])

print(stock)