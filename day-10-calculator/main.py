from calculator_art import logo
from replit import clear

def add(n1,n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 * n2

def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    num1 = int(input("What's the first number? "))
    for operand in operations:
        print(operand)

    should_continue = True
    while should_continue:
        operand = input("Pick an operation from above: ")
        num2 = int(input("What's the next number? "))

        calculation_function = operations[operand]
        result = calculation_function(num1,num2)

        print(f"\n{num1} {operand} {num2} = {result}\n")

        user_action = input(f"Select:\n(1) Continue calculating with {result}\n(2) Start a fresh calculation\nOr any other key to quit\n")
        
        if user_action == '1':
            num1 = result
        elif user_action == '2':      
            should_continue = False
            clear()
            calculator()
        else:
            should_continue = False
            print("Exiting. Have a good day!")

print(logo)
calculator()