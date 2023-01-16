width = int(input())
length = int(input())
height = int(input())
volume = width * length * height
sum_peaces = 0

boxes = input()
while boxes != "Done":
    a = int(boxes)
    sum_peaces = sum_peaces + a
    if volume < sum_peaces:
        break
    boxes = input()

delta = abs(volume - sum_peaces)
if sum_peaces > volume:
    print(f"No more free space! You need {delta} Cubic meters more.")
else:
    print(f"{delta} Cubic meters left.")
