# . "room for one person" – 18.00 лв за нощувка
# • "apartment" – 25.00 лв за нощувка
# • "president apartment" – 35.00 лв за нощувка
days = float(input())
room = str(input())
evaluation = str(input())

room_for_one_person = 18.00 * (days-1)
apartment = 25.00 * (days-1)
president_apartment = 35.00 * (days-1)
total = 0
if room == "room for one person":
    total = room_for_one_person
elif room == "apartment":
    if days > 15:
        total = apartment - apartment * 0.50
    elif 10 <= days <=15:
        total = apartment - apartment * 0.35
    elif days < 10:
        total = apartment - apartment * 0.30
elif room == "president apartment":
    if days > 15:
        total = president_apartment - president_apartment * 0.20
    elif 10 <= days <=15:
        total = president_apartment - president_apartment * 0.15
    elif days < 10:
        total = president_apartment - president_apartment * 0.10

if evaluation == "positive":
    total = total + total*0.25
elif evaluation == "negative":
    total = total - total*0.10

print(f"{total:.2f}")
