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

This version contains
- variables
- input
- if-else statements

The code for Version 1 of the calculator is as follows:
```py
#VERSION 1
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

The program runs in a while loop until the user decides to exit, and it contains error handling for invalid inputs.

This version contains
- 6 functions with parameters
- if-else statements
- while loop
- conditional expression

The code for Version 2 of the calculator is as follows:
```py
# version 2
def add(a, b): # a and b are perimeters
    print("\nAddition")
    answer = a + b
    print(f"\t{a} + {b} = {answer}\n")

def sub(a, b):
    print("\nSubtraction")
    answer = a - b
    print(f"\t{a} - {b} = {answer}\n")

def mul(a, b):
    print("\nMultiplication")
    answer = a * b
    print(f"\t{a} * {b} = {answer}\n")

def div(a, b):
    print("\nDivision")
    answer = a / b
    print(f"\t{a} / {b} = {answer}\n")

def mod(a, b):
    print("\nModulus")
    answer = a % b
    print(f"\t{a} % {b} = {answer}\n")

def expo(a, b):
    print("\nExponential")
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

    a = int(input("Input first number: "))
    b = int(input("Input second number: "))

    if choice == "a" or choice == "A":
        add(a, b)

    elif choice == "b" or choice == "B":
        sub(a, b)

    elif choice == "c" or choice == "C":
        mul(a, b)

    elif choice == "d" or choice == "D":
        div(a, b)

    elif choice == "e" or choice == "E":
        expo(a, b)

    elif choice == "f" or choice == "F":
        mod(a, b)

    elif choice == "g" or choice == "G":
        print("\nProgram end")
        quit()

    else:
        print("\nInvalid operator")

```
## Version 3: [Code link](calculator_thirdversion.py)

This version contains
- dictionary
- for loop
- while loop
- functions with parameters and arguments

```python
# VERSION 3
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2
  
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def start():
  num1 = float(input("What's the first number? "))
  # to print the keys or operators in operations dictionary
  for operators in operations:
    print(operators)

  should_continue = True
  while should_continue:
      operation_symbol = input("Choose an operation: ")
      num2 = float(input("What's the next number? "))
      # to get the value in a operations dictionary (e.g. the operation_symbol == +, it will then go to dictionary to search for the value of add, since the operation_symbol is the key)
      calculation_function = operations[operation_symbol]
      # e.g the calculation_function = add, it will then go to the add functions to sum it using the argument of num1 and num2
      answer = calculation_function(num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")
    
      choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to exit, or type 's' to restart: ")
      if choice == 'y':
        num1 = answer
      elif choice == 'n':
        should_continue = False
      else:
        should_continue = False
        start() #recursive function 
start()
```