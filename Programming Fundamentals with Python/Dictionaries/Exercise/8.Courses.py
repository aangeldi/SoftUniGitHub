data = input()
school = {}

while data != "end":
    split_data = data.split(" : ")
    course = split_data[0]
    student = split_data[1]

    if course not in school:
        students = []
        school[course] = students
        school[course].append(student)
    else:
        school[course].append(student)

    data = input()

for course_name, students in school.items():
    print(f"{course_name}: {len(students)}")
    for student in school[course_name]:
        print(f"-- {student}")