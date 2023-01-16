name = input()
clas = 1
sum_grades = 0
excluded = 0
while clas <= 12:
    year_grade = float(input())
    if year_grade < 4:
        excluded += 1
        if excluded > 1:
            print(f'{name} has been excluded at {clas - 1} grade')
            break

    sum_grades += year_grade
    clas += 1

average = sum_grades / 12
if excluded <= 1:
    print(f'{name} graduated. Average grade: {average:.2f}')