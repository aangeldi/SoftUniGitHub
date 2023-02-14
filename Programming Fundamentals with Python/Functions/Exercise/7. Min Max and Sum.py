def numbers(list_of_numbers):
    min_num = min(list_of_numbers)
    max_num = max(list_of_numbers)
    sum_num = sum(list_of_numbers)
    return [min_num, max_num, sum_num]


nums = [int(x) for x in input().split()]
result = numbers(nums)
print(f"The minimum number is {result[0]}")
print(f"The maximum number is {result[1]}")
print(f"The minimum number is {result[2]}")

