import math

first = int(input())
second = int(input())
third = int(input())

sum = (first + second + third)
intiger = (sum//60)
flo = (sum%60)
intiger = math.floor(intiger)

if (flo < 10):
    print(f"{intiger}:0{flo}")
else:
    print(f"{intiger}:{flo}")

