from calculator_art import logo

print(logo)




def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {'+': add, '-': subtract, '*': multiply, '/' :divide}

first_number = int(input("What is the first number?: "))

for symbols in operations:
    print(symbols)

pick_operation = input("Select an Operation from the line above: ")
second_number = int(input("What is the second number?: "))

calculation_function = operations[pick_operation]
answer = calculation_function(first_number, second_number)

print(f"{first_number} {pick_operation} {second_number} = {answer}")