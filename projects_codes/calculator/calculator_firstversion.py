num1 = float(input("Enter a number: "))
operators = input("Select an operator [+, -, /, *, **, %, //]: ")
num2 = float(input("Enter a number: "))

if operators == "+":
    print(num1 + num2)
elif operators == "-":
    print(num1 - num2)
elif operators == "/":
    print(num1 / num2)
elif operators == "**":
    print(num1 ** num2)
elif operators == "*":
    print(num1 * num2)
elif operators == "%":
    print(num1 % num2)
elif operators == "//":
    print(num1 // num2)
else:
    print("Invalid operator")