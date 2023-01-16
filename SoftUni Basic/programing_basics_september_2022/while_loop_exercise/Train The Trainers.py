juri = int(input())
command = input()
full_average = 0
count_command = 0
while command != "Finish":
    average = 0
    sum = 0
    counter = 0

    for i in range(1, juri + 1):
        num = float(input())
        sum = sum + num
        counter += 1

    average = sum/counter
    print(f"{command} - {average:.2f}.")
    command = input()
    full_average = full_average + average
    count_command += 1

full_average = full_average / count_command
print(f"Student's final assessment is {full_average:.2f}.")
