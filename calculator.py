num1 = int(input("Enter first number: "))
operator = input("Enter operation (+, -, *, /): ")
num2 = int(input("Enter second number: "))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error!."
else:
    result = "Invalid operation."
print("Result:", result)
