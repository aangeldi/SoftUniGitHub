shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    current_command = command[0]
    product = command[1]

    if current_command == "Urgent":
        if product not in shopping_list:
            shopping_list.insert(0, product)
    elif current_command == "Unnecessary":
        if product in shopping_list:
            shopping_list.remove(product)
    elif current_command == "Correct":
        if product in shopping_list:
            idx = shopping_list.index(product)
            shopping_list[idx] = command[2]
    elif current_command == "Rearrange":
        if product in shopping_list:
            shopping_list.remove(product)
            shopping_list.append(product)

    command = input()
print(", ".join(shopping_list))
