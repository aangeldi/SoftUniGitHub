numbers = [int(x) for x in input().split(", ")]
low_boundary = 1
high_boundary = 10

while numbers:
    num = [x for x in numbers if low_boundary <= x <= high_boundary]
    print(f"Group of {high_boundary}'s: {num}")

    for el in num:
        numbers.remove(el)

    low_boundary += 10
    high_boundary += 10
