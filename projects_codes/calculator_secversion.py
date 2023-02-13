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
