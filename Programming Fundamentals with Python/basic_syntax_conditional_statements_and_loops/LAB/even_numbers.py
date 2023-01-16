n = int(input())

for i in range(n):
    numers = int(input())
    if numers % 2 != 0:
        print(f"{numers} is odd!")
        break
else:
    print("All numbers are even.")