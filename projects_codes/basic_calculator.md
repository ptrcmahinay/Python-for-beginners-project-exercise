# Basic Calculator

## What I learned when creating calculator

1. Fundamentals of Python programming, including data types, variables, functions, and control structures.
2. How to take input from the user and process it to perform mathematical operations.
3. How to use conditional statements to handle different cases, such as addition, subtraction, multiplication, division, modulus, and exponential operations.
4. How to write and call functions in Python, including the use of function parameters and return values.
5. How to use loops to run the calculator continuously until the user decides to exit.
6. How to format and display the results of the calculations to the user.

This is a basic calculator program written in Python. There are two versions available:

## Version 1: [Code link](/projects_codes/calculator_firstversion.py)
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
## Version 2: [Code link](/projects_codes/calculator_secversion.py)
This version allows also a user to perform different mathematical operations (addition, subtraction, multiplication, division, modulus, and exponentiation) on two numbers. The program runs in a while loop until the user decides to exit, and it contains error handling for invalid inputs.

***Uses:*** functions, while loops and conditional expressions. 

## Version 3: [Code link](/projects_codes/calculator_thirdversion.py)
This version not only allows the user to type a two input but also it allows the user to continue the calculation. It has the option to continue, exit and restart the calculation.

***Uses:*** Dictionary, if/elif/else, While loop, Flag, return function, Functions, Recursive functions.