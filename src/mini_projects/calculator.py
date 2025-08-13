# Python calculator

operator = input("Enter an operator (+ , - , * , / , % ): ")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if operator == '+':
    r = num1 + num2
    print(r)
elif operator == '-':
    r = num1 - num2
    print(r)
elif operator == '*':
    r = num1 * num2
    print(r)
elif operator == '/':
    r = num1 / num2
    print(r)
elif operator == '%':
    r = num1 % num2
    print(r)
else:
    print("Enter a valid operator!")
