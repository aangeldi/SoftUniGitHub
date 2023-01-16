command = str(input())
counter_student = 0
counter_standard = 0
counter_kid = 0

while command != "Finish":
    total = 0
    percent_student = 0
    percent_standard = 0
    percent_kid = 0
    counter_student1 = 0
    counter_standard1 = 0
    counter_kid1 = 0
    free_places = int(input())
    type_ticket = str(input())
    while type_ticket != "End" and type_ticket != "Finish":
        for i in range(1, free_places + 1):
            if type_ticket == "student":
                counter_student += 1
                counter_student1 += 1
                percent_student = (counter_student1 / free_places) * 100
            elif type_ticket == "standard":
                counter_standard += 1
                counter_standard1 += 1
                percent_standard = (counter_standard1 / free_places) * 100
            elif type_ticket == "kid":
                counter_kid += 1
                counter_kid1 += 1
                percent_kid = (counter_kid1 / free_places) * 100
            else:
                break
            type_ticket = input()
    total = percent_student + percent_standard + percent_kid
    print(f"{command} - {total:.2f}% full.")
    if type_ticket != "Finish":
        command = str(input())
    else:
        command = type_ticket
total_tickets = counter_student + counter_standard + counter_kid
print(f"Total tickets: {total_tickets}")
print(f"{counter_student/total_tickets * 100:.2f}% student tickets.")
print(f"{counter_standard/total_tickets * 100:.2f}% standard tickets.")
print(f"{counter_kid/total_tickets * 100:.2f}% kids tickets.")
