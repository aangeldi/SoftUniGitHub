def characters(a, b):
    new_list_numbers = []
    for i in range(ord(a) + 1, ord(b)):
        new_list_numbers.append(chr(i))
    listed = " ".join(new_list_numbers)
    return listed


char1 = input()
char2 = input()
print(characters(char1, char2))
