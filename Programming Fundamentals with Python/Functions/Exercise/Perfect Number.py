def digit(num):
    sum = 0
    for i in range(1, num - 1):
        if num % i == 0:
            sum += i
    if num == sum:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
digit(number)
