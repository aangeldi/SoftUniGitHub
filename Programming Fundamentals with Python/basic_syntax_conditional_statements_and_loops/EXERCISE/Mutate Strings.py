first_string = str(input())
second_string = str(input())
result = ""
for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        result = second_string[:i + 1] + first_string[i+ 1:]
        print(result)
    else:
        continue
