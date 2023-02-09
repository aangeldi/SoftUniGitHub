n = int(input())
temp = 0
value = 0
a = 0
b = 0
c = 0
d = 0
for i in range(1, n + 1):
    w = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = (w // snowball_time) ** snowball_quality
    if value > temp:
        a = w
        b = snowball_time
        c = snowball_quality
        d = value
        temp = value

print(f"{a} : {b} = {d} ({c})")
