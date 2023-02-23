def is_num_in_seq(el):
    if el in sequence_numbers:
        return True
    return False


sequence_numbers = [int(x) for x in input().split()]

command_args = input()

while command_args != "Finish":
    command = command_args.split()[0]

    if command == "Add":
        number = int(command_args.split()[1])
        sequence_numbers.append(number)
    elif command == "Remove":
        number = int(command_args.split()[1])
        if is_num_in_seq(number):
            number = int(command_args.split()[1])
            sequence_numbers.remove(number)
    elif command == "Replace":
        number = int(command_args.split()[1])
        if is_num_in_seq(number):
            replacement = int(command_args.split()[2])
            idx = sequence_numbers.index(number)
            sequence_numbers.pop(idx)
            sequence_numbers.insert(idx, replacement)
    elif command == "Collapse":
        number = int(command_args.split()[1])
        sequence_numbers = [x for x in sequence_numbers if x > number]

    command_args = input()

result = [str(a) for a in sequence_numbers]
print(' '.join(result))
