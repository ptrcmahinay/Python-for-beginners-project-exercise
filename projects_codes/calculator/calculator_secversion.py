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
