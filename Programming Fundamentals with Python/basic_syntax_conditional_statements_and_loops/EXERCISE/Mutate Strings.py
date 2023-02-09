first_string = "samocska"
second_string ="kzlewcki"
result = ""
for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        result = second_string[:i + 1] + first_string[i+ 1:]
        print(result)
    else:
        continue
