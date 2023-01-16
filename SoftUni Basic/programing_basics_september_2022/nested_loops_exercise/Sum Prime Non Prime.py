sum_prime = 0
sum_non_prime = 0
command = input()

while command != "stop":
    num = int(command)
    counter_prime = 0
    if num < 0:
        print("Number is negative.")
    for i in range(1, num + 1):
        if num % i == 0:
            counter_prime = counter_prime + 1

    if counter_prime == 2:
        sum_prime = sum_prime + num
    elif counter_prime != 2 and num > 0:
        sum_non_prime = sum_non_prime + num

    command = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
