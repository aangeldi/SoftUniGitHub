def sum_even_odd(txt):
    sum_even = 0
    sum_odd = 0
    for i in range(len(txt)):
        if int(txt[i]) % 2 == 0:
            sum_even += int(txt[i])
        else:
            sum_odd += int(txt[i])
    list_elements = [sum_odd, sum_even]
    return list_elements


string = input()
result = sum_even_odd(string)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")
