num1 = float(input("Enter first number: \n"))
op = input("Enter operator: ")
num2 = float(input("Enter second number: \n"))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '/':
    print(num1 / num2)
elif op == '*':
    print(num1 * num2)
else:
    print("Please provide a valid operator")
