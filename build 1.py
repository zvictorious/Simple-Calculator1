
num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
operation = input("Enter your desired operation: ")
result1 = float(num1) + float(num2)
result2 = float(num1) - float(num2)
result3 = float(num1) * float(num2)
result4 = float(num1) / float(num2)
if operation == "+":
    print(result1)
elif operation == "-":
    print(result2)
elif operation == "*":
    print(result3)
elif operation == "/":
    print(result4)
