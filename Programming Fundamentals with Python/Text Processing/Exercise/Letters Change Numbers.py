import string

alphabet_lowercase = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)

data = input().split()
position = 0
first_result = 0
result = 0

for el in data:
    number = (int(el[1:-1]))
    if el[0] in alphabet_upper:
        for idx, value in enumerate(alphabet_upper):
            if value == el[0]:
                position = idx + 1
                first_result = number / position
                break
        if el[-1] in alphabet_lowercase:
            for idx, value in enumerate(alphabet_lowercase):
                if value == el[-1]:
                    position = idx + 1
                    first_result += position
        else:
            for idx, value in enumerate(alphabet_upper):
                if value == el[-1]:
                    position = idx + 1
                    first_result -= position
    else:
        for idx, value in enumerate(alphabet_lowercase):
            if value == el[0]:
                position = idx + 1
                first_result = number * position
                break
        if el[-1] in alphabet_upper:
            for idx, value in enumerate(alphabet_upper):
                if value == el[-1]:
                    position = idx + 1
                    first_result -= position
        else:
            for idx, value in enumerate(alphabet_lowercase):
                if value == el[-1]:
                    position = idx + 1
                    first_result += position

    result += first_result

print(f"{result:.2f}")
