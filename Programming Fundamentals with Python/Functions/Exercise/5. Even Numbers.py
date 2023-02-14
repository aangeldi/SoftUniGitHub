def even_numbers(numbers):
    return numbers % 2 != 0


nums = [int(num) for num in input().split()]
print(list(filter(even_numbers, nums)))
