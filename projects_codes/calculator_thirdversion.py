#Calculator

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