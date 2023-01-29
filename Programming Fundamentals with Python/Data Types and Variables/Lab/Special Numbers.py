# Write a program that reads an integer n.
# Then, for all numbers in the range [1, n], prints the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.

num = int(input())

for n in range(1, num + 1):
    sum_of_digits = 0
    digit = 0
    m = n
    while m > 0:
        digit = m % 10
        m = m // 10
        sum_of_digits += digit
        digit = 0
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")
