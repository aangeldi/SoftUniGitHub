# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
number_of_the_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())
student_attendances = []
max_attendances = 0
for _ in range(number_of_the_students):

    student_attendances = (int(input()))
    max_attendances = max(max_attendances, student_attendances)

# max_student_attendances = max(student_attendances)
total_bonus = 0
if number_of_the_lectures != 0:
    total_bonus = max_attendances / number_of_the_lectures * (5 + additional_bonus)
print(f"Max Bonus: {round(total_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")
