entry = input()
exam = {}
banned_user = []
points = 0
while entry != "exam finished":
    entry = entry.split("-")
    username = entry[0]
    language = entry[1]

    if language == "banned":
        banned_user.append(username)
    else:
        points = entry[2]

    if language not in exam:
        results = []
        exam[language] = {}
        results.append(int(points))
        exam[language][username] = results
    else:
        if username not in exam[language]:
            results = []
            results.append(int(points))
            exam[language][username] = results
        else:
            results.append(int(points))
            exam[language][username] = results

    entry = input()

print("Results:")
for key, value in exam.items():
    for el, point in value.items():
        if el in banned_user:
            continue
        else:
            print(f"{el} | {max(point)}")

print("Submissions:")
for key, value in exam.items():
    apearence = 0
    for el, point in value.items():
        apearence += len(point)
    if key != "banned":
        print(f"{key} - {apearence}")
