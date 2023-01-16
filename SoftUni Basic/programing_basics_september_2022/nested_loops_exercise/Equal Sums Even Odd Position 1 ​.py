num_1 = int(input())
num_2 = int(input())

units = 0
tens = 0
hundreds = 0
thousands = 0
ten_thousands = 0
hundred_thousands = 0

sum_odd = 0
sum_even = 0

for i in range(num_1, num_2 + 1):
    hundred_thousands = i // 100000
    ten_thousands = i // 10000
    thousands = i // 1000
    hundreds = i // 100
    tens = i // 10
    units = i
    sum_odd = hundred_thousands % 10 + thousands % 10 + tens % 10
    sum_even = ten_thousands % 10 + hundreds % 10 + units % 10
    if sum_odd == sum_even:
        print(str(i) + " ", end="")


