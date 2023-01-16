exam_hours = int(input())
exam_minutes = int(input())
arrive_hours = int(input())
arrive_minutes = int(input())

convert_exam_hours = exam_hours*60 + exam_minutes
convert_arrive_hours = arrive_hours*60 + arrive_minutes
dif1f_min = abs(convert_exam_hours - convert_arrive_hours)

if convert_arrive_hours > convert_exam_hours:
    print("Late")
    if dif1f_min >= 60:
        hour = dif1f_min // 60
        mins = dif1f_min % 60
        print(f"{hour}:{mins:02d} hours after the start")
    else:
        print(f"{dif1f_min} minutes after the start")
elif convert_arrive_hours == convert_exam_hours or dif1f_min <= 30:
    print("On time")
    if dif1f_min > 0:
        print(f"{dif1f_min} minutes before the start")
else:
    print("Early")
    if dif1f_min >= 60:
        hour = dif1f_min // 60
        mins = dif1f_min % 60
        print(f"{hour}:{mins:02d} hours before the start")
    else:
        print(f"{dif1f_min} minutes before the start")
