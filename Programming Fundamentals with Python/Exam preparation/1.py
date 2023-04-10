stops = input()

while True:
    commands = input()

    # for command in commands:
    if "Add Stop" in commands:
        _, index, string = commands.split(":")
        index = int(index)
        if 0 <= index <= len(stops):
            stops = stops[:index] + string + stops[index:]
    elif "Remove Stop" in commands:
        _, start_index, end_index = commands.split(":")
        start_index = int(start_index)
        end_index = int(end_index)
        if 0 <= start_index <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index+1:]
    elif "Switch" in commands:
        _, old_string, new_string = commands.split(":")
        stops = stops.replace(old_string, new_string)
    elif "Travel" in commands:
        print(f"Ready for world tour! Planned stops: {stops}")
        break
    print(f"{stops}")

