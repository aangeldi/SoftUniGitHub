factor = int(input())
count = int(input())
result = []
temp = 0

for i in range(count):
    temp = temp + factor
    result.append(temp)
print(result)