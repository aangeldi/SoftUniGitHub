data = input().upper()
strings = []
string = ""
number = ""
numbers = []

for i in range(len(data)):
    if not data[i].isdigit():
        string += data[i]
        if data[i + 1].isdigit():
            strings.append(string)
            string = ""
    else:
        number += data[i]
        if not data[i + 1].isdigit():
            numbers.append(number)
            number = ""

    if i == len(data) - 2:
        numbers.append(data[len(data) - 1:])
        break

unique = set("".join(strings))
print(f"Unique symbols used: {len(unique)}")

for i in range(len(strings)):
    print(f"{strings[i] * int(numbers[i])}", end="")
