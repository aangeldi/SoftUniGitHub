import re

data = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

result = re.finditer(pattern, data)

for res in result:
    print(res.group(), end=" ")

