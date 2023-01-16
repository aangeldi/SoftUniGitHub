n_groups = int(input())

musala = 0
percent_musala = 0
monblan = 0
percent_monblan = 0
kilimanjaro = 0
percent_kilimanjaro = 0
K2 = 0
percent_K2 = 0
everest = 0
percent_everest = 0
total_sum = 0
for i in range (1, n_groups + 1):
    people = int(input())
    total_sum = total_sum + people
    if 0 < people <= 5:
        musala = people + musala
    elif 5 < people <= 12:
        monblan = people + monblan
    elif 12 < people <= 25:
        kilimanjaro = people + kilimanjaro
    elif 25 < people <= 40:
        K2 = people + K2
    elif people > 40:
        everest = people + everest

percent_musala = (musala/total_sum) * 100
print(f"{percent_musala:.2f}%")
percent_monblan = (monblan / total_sum) * 100
print(f"{percent_monblan:.2f}%")
percent_kilimanjaro = (kilimanjaro / total_sum) * 100
print(f"{percent_kilimanjaro:.2f}%")
percent_K2 = (K2 / total_sum) * 100
print(f"{percent_K2:.2f}%")
percent_everest = (everest / total_sum) * 100
print(f"{percent_everest:.2f}%")