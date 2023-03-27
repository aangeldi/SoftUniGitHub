command = int(input())
registered = {}

for _ in range(command):
    commands = input().split()
    user_name = commands[1]
    registration = commands[0]

    if registration == 'register':
        license_number = commands[2]

        if user_name not in registered:
            registered[user_name] = license_number
            print(f"{user_name} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")
    else:
        if user_name not in registered:
            print(f"ERROR: user {user_name} not found")
        else:
            del registered[user_name]
            print(f"{user_name} unregistered successfully")

for user,license in registered.items():
    print(f"{user} => {license}")
