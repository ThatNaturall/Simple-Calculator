# Method for adding
def add(num1, num2):
    return num1 + num2

# Method for subtraction 
def subtraction(num1, num2):
    return num1 - num2

# Method for multiplication
def multiplication(num1, num2):
    return num1 * num2

# Method for division
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Can't divide by 0"

def operation(op, num1, num2):
    if op == '+':
        return add(num1, num2)
    elif op == '-':
        return subtraction(num1, num2)
    elif op == '*':
        return multiplication(num1, num2)
    elif op == '/':
        return division(num1, num2)
    else:
        return "Invalid Operator"

calculate = True

while calculate:
    num1 = float(input('Enter first number: '))
    op = input('Enter Operator (+, -, *, /): ')
    num2 = float(input('Enter the second number: '))
    print(num1, num2, op)
    result = operation(op, num1, num2)
    print(f"{num1} {op} {num2} = {result}")
    yes_or_no = input('Continue? (Y/N)')

    if yes_or_no.upper() == 'N':
        calculate = False
