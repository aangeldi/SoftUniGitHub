data = input()
strings = ""
digits = ""
others = ""

for i in range(len(data)):
    if data[i].isalpha():
        strings += data[i]
    elif data[i].isdigit():
        digits += data[i]
    else:
        others += data[i]
print(digits)
print(strings)
print(others)