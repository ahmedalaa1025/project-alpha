number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

try:
    result = number1 / number2
    print(result)
except ZeroDivisionError:
    print("You cannot divide by zero.")