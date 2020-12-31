# 100 Days of Code
# Calculator

from art import logo

# add
def add(n1, n2):
  return n1 + n2

# subtract
def subtract(n1, n2):
  return n1 - n2

# multiply
def multiply(n1, n2):
  return n1 * n2

# divide
def divide(n1, n2):
  return n1 / n2

# dictionary to store calculation operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

# main calculator logic
def calculator():
  print(logo)

  num1 = float(input("Whats the first number?: "))

  calculating = True
  while calculating:

    for symbol in operations:
      print(symbol)

    operation_symbol = input("Which operation would you like to perform?: ")

    num2 = float(input("Whats the second number?: "))

    # dictionary 'operations' is used here to call the actual function that performs the math
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # ending flow control
    cont = input(f"Type 'y to continue calculating with {answer} or type 'n' to start a new calucation: ")
    if cont == "y":
      num1 = answer
    else:
      calculator() # function call to itself if user wants to start from scratch

calculator()