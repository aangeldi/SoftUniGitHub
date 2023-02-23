command = input()
to_do_list = [0]*10

while command != "End":
    importance, task = command.split("-")
    index = int(importance) - 1
    to_do_list.pop(index)
    to_do_list.insert(index, task)
    # to_do_list[index] = task
    command = input()

print([index for index in to_do_list if index != 0])