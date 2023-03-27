num = int(input())
students = {}

for _ in range(num):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        grades = []
        students[student_name] = grades
        students[student_name].append(grade)
    else:
        students[student_name].append(grade)

for student, grade in students.items():
    sum = 0
    average = 0
    for i in range(len(students[student])):
        sum += float(students[student][i])
    average = float(sum / len(students[student]))
    if average >= 4.50:
        print(f"{student} -> {average:.2f}")

