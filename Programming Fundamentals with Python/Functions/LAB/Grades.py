# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"


def graduation(digit):
    if 2.00 <= digit <= 2.99:
        return "Fail"
    elif 3.00 <= digit <= 3.49:
        return "Poor"
    elif 3.50 <= digit <= 4.49:
        return "Good"
    elif 4.50 <= digit <= 5.49:
        return "Very Good"
    elif 5.50 <= digit <= 6.00:
        return "Excellent"


grade_mark = float(input())
a = graduation(grade_mark)
print(a)
