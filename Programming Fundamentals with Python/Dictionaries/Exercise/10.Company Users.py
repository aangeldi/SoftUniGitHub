data = input()
employees = {}

while data != "End":
    company, employee_id = data.split(" -> ")

    if company not in employees:
        ids = []
        employees[company] = ids
        employees[company].append(employee_id)
    else:
        if employee_id not in employees[company]:
            employees[company].append(employee_id)

    data = input()

for name, id in employees.items():
    print(name)
    for i in employees[name]:
        print(f"-- {i}")

