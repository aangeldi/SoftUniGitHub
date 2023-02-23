n_wagons = int(input())
train = [0] * n_wagons

input_string = input().split()
command = input_string[0]

while command != "End":
    index = int(input_string[1])
    if command == "add":
        train[-1] += index
    elif command == "insert":
        index = int(input_string[1])
        people = int(input_string[2])
        train[index] += people
    elif command == "leave":
        index = int(input_string[1])
        people = int(input_string[2])
        train[index] -= people

    input_string = input().split()
    command = input_string[0]
print(train)