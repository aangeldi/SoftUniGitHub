import random
quatar_finals = []
teams = ["CSKA", "levski", "botev", "slavia", "ludogorets", "loko", "beroe", "cherno more"]
length = int(len(teams) / 2)
for i in range(length):
    random_element1 = random.choice(teams)
    quatar_finals.append(random_element1)
    teams.remove(random_element1)

    random_element2 = random.choice(teams)
    quatar_finals.append(random_element2)
    teams.remove(random_element2)


a = random.randint(1, 4)
b = random.randint(1, 4)
while b == a:
    b = random.randint(1, 4)


print(quatar_finals)
print(a)
print(b)