student = input()
average_mark = 0
count = 0
excluded = 0

while True:
    assessment = float(input())
    count += 1
    if assessment < 4:
        excluded = excluded + 1
        if excluded == 2:
            print(f"{student} has been excluded at {count} grade")
            break
        count = count - 1
    else:
        average_mark = average_mark + assessment

    if count == 12:
        average_mark = average_mark/12
        print(f"{student} graduated. Average grade: {average_mark:.2f}")
        break

