people_phone = str(input())
dictionary = {}
counter = 0
while len(people_phone) > 1:
    list_dictionary = people_phone.split("-")
    name = list_dictionary[0]
    phone = list_dictionary[1]
    dictionary[name] = phone

    people_phone = str(input())

for _ in range(int(people_phone)):
    search_name = input()
    if search_name in dictionary.keys():
        print(f"{search_name} -> {dictionary[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
