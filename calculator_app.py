# Task 1: functions for each arithmetic op
# created functions such that they can handle operations with multiple arguments in the future

def add(*args):
    sum = 0
    for a in args:
        sum += a
    return sum

def subtract(num1, *args):
    result = num1
    for a in args:
        result -= a
    return result

def multiply(*args):
    result = 0
    for a in args:
        result *= a
    return result

def divide(num1, *args):
    result = num1
    for a in args:
        if a == 0:
            print("Error: cannot divide by 0!")
            a = input("Enter a new number to divide by")
            if("." in a):
                a = float(a)
            else:
                a = int(a)
        result /= a
    return result

#Task 2
''' For simplicity and based on assignment description, currently assuming only 2 numbers as input for operations. \
    Based on the function definitions, this can be extended to operations on multiple number arguments in the future
'''

operation_select = input("Select operation: + - * /")
number1 = input("Enter first number:")
if("." in number1):
    number1 = float(number1)
else:
    number1 = int(number1)

number2 = input("Enter second number:")
if("." in number2):
    number2 = float(number2)
else:
    number2 = int(number2)

if operation_select  == "+":
    print(add(number1, number2))
elif operation_select == "-":
    print(subtract(number1, number2))
elif operation_select == "*":
    print(multiply(number1, number2))
elif operation_select == "/":
    print(divide(number1, number2))
else:
    print("Error - Could not perform operation! Check your syntax")

# Task 3

''' See above code for added handling of the following possible errors \
    Division by zero (line 24) \
    Invalid input for operation and numbers (line 60) \
    Handling both float and int inputs (line 40, 46, 27)
'''
