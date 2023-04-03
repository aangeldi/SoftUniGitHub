import re

numbers = []

while True:
    data = input()
    if not data:
        break
    pattern = r'\d+'
    result = re.findall(pattern, data)
    numbers.extend(result)

print(" ".join(numbers))
