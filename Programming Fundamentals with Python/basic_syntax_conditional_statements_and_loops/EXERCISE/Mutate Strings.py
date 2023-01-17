first_string = str(input())
second_string = str(input())

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        first_string = first_string.replace(first_string[i], second_string[i], 1)
        print(first_string)
