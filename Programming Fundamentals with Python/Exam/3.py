records = {}

while True:
    line = input()

    if line == "Log out":
        break

    command_args = line.split(": ")
    command = command_args[0]

    if command == "New follower":
        username = command_args[1]
        if username in records:
            continue
        else:
            records[username] = 0
    elif command == "Like":
        username = command_args[1]
        likes = int(command_args[2])
        if username in records:
            records[username] += likes
        else:
            records[username] = likes
    elif command == "Comment":
        username = command_args[1]
        if username in records:
            records[username] += 1
        else:
            records[username] = 1
    elif command == "Blocked":
        username = command_args[1]
        if username in records:
            del records[username]
        else:
            print(f"{username} doesn't exist.")

print(f"{len(records.keys())} followers")
for (key, value) in records.items():
    print(f"{key}: {value}")