import re

data = input()
pattern = r"\b_([a-zA-Z\d]+)\b"
result = re.findall(pattern, data)

print(*result, sep=",")


