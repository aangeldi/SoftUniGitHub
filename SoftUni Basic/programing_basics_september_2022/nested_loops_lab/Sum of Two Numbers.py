first_num = int(input())
second_num = int(input())
magic_num = int(input())
sum = 0
counter = 0
all_counter = 0

for i in range(first_num, second_num + 1):
    for j in range(first_num, second_num + 1):
        sum = i + j
        if sum == magic_num and counter == 0:
            counter = all_counter + 1
            k = i
            l = j
        all_counter = all_counter + 1

if counter != 0:
    print(f"Combination N:{counter} ({k} + {l} = {magic_num})")
else:
    print(f"{all_counter} combinations - neither equals {magic_num}")