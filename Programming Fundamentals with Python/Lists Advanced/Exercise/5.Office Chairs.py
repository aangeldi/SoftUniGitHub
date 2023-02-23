number_of_rooms = int(input())
chairs_amount = 0
people_amount = 0

for i in range(number_of_rooms):
    chairs_visitors = input().split()
    chairs = chairs_visitors[0]
    people = int(chairs_visitors[1])
    chairs_amount += len(chairs)
    people_amount += people
    if people > len(chairs):
        print(f"{people - len(chairs)} more chairs needed in room {i + 1}")

if chairs_amount >= people_amount:
    print(f"Game On, {chairs_amount - people_amount} free chairs left")
