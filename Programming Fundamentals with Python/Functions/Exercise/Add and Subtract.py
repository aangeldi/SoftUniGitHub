def sum_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


first = int(input())
second = int(input())
third = int(input())


print(subtract_numbers(sum_numbers(first, second), third))
