def calculation(operator, num1, num2):
    result = None
    if operator == "multiply":
        result = num1 * num2
        return result
    elif operator == "divide":
        result = num1 // num2
        return result
    elif operator == "add":
        result = num1 + num2
        return result
    elif operator == "subtract":
        result = num1 - num2
        return result


op = str(input())
nu = int(input())
num = int(input())

print(calculation(op, nu, num))
