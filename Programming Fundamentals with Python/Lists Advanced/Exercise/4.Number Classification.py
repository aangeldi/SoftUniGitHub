list_numbers = [int(x) for x in input().split(", ")]
positive = []
negative = []
even = []
odd = []
for num in list_numbers:
    if num % 2 == 0:
        even.append(num)
    if num >= 0:
        positive.append(num)
    if num < 0:
        negative.append(num)
    if num % 2 != 0:
        odd.append(num)
positive = [str(x) for x in positive]
positive = ", ".join(positive)
negative = [str(x) for x in negative]
negative = ", ".join(negative)
even = [str(x) for x in even]
even = ", ".join(even)
odd = [str(x) for x in odd]
odd = ", ".join(odd)
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")
