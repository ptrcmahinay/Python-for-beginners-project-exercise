# Basic Calculator

## What I learned when creating calculator

1. Fundamentals of Python programming, including data types, variables, functions, and control structures.
2. How to take input from the user and process it to perform mathematical operations.
3. How to use conditional statements to handle different cases, such as addition, subtraction, multiplication, division, modulus, and exponential operations.
4. How to write and call functions in Python, including the use of function parameters and return values.
5. How to use loops to run the calculator continuously until the user decides to exit.
6. How to format and display the results of the calculations to the user.

This is a basic calculator program written in Python. There are two versions available:

## Version 1: [Code link](calculator_firstversion.py)
This version of the calculator allows you to perform basic arithmetic operations such as addition, subtraction, multiplication, division, exponentiation, modulo, and floor division between two numbers.

The user is prompted to enter the first number and then the operator to be used for the calculation, followed by the second number. The code then uses an if-elif statement to determine which operator the user has selected and performs the corresponding calculation. If an invalid operator is entered, the code will print "Invalid operator."

The code for Version 1 of the calculator is as follows:
```py
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
```
## Version 2: [Code link](calculator_secversion.py)
This version allows also a user to perform different mathematical operations (addition, subtraction, multiplication, division, modulus, and exponentiation) on two numbers.

It uses functions, loops and conditional expressions. The program runs in a while loop until the user decides to exit, and it contains error handling for invalid inputs.

The code for Version 2 of the calculator is as follows:
```py
def add(a, b): # a and b are perimeters
    answer = a + b
    print(f"\t{a} + {b} = {answer}\n")

def sub(a, b):
    answer = a - b
    print(f"\t{a} - {b} = {answer}\n")

def mul(a, b):
    answer = a * b
    print(f"\t{a} * {b} = {answer}\n")

def div(a, b):
    answer = a / b
    print(f"\t{a} / {b} = {answer}\n")

def mod(a, b):
    answer = a % b
    print(f"\t{a} % {b} = {answer}\n")

def expo(a, b):
    answer = a ** b
    print(f"\t{a} ** {b} = {answer}\n")

#def num(a, b):
while True:
    print("\nA. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exponentiation")
    print("F. Modulus")
    print("G. Exit")

    choice = input("\nChoose a letter: ")

    if choice == "a" or choice == "A":
        print("\nAddition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a, b)

    elif choice == "b" or choice == "B":
        print("\nSubtraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub(a, b)

    elif choice == "c" or choice == "C":
        print("\nMultiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        mul(a, b)

    elif choice == "d" or choice == "D":
        print("\nDivision")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        div(a, b)

    elif choice == "e" or choice == "E":
        print("\nExponential")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        expo(a, b)

    elif choice == "f" or choice == "F":
        print("\nModulus")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        mod(a, b)

    elif choice == "g" or choice == "G":
        print("\nProgram end")
        quit()

    else:
        print("\nInvalid operator")

```
