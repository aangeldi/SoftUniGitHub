data = input()
courses = {}

while ":" in data:
    name, id, course = data.split(":")
    if course not in courses:
        courses[course] = {id: name}
    else:
        courses[course][id] = name

    data = input()

data = data.split("_")
data = " ".join(data)
for key, value in courses.items():
    if data == key:
        for ID, student_name in value.items():
            print(f"{student_name} - {int(ID)}")

