import math

h = int(input())
mi = int(input())

miut = int((h*60) + mi)
min_after_delay = miut + 15
hour = min_after_delay // 60
mins = min_after_delay % 60
hour = math.floor(hour)

if (hour==24):
    hour = 0

if mins < 10:
    print(f"{hour}:0{mins}")
else:
    print(f"{hour}:{mins}")
