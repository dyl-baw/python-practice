from calculator_art import logo






def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract, 
    '*': multiply,
    '/' :divide
}



calculate = True
def calculator():
    print(logo)
    first_number = float(input("What is the first number?: "))

    for symbols in operations:
        print(symbols)
    calculate = True
    while calculate:
        pick_operation = input("Select an Operation from the line above: ")
        second_number = float(input("What is the second number?: "))

        calculation_function = operations[pick_operation]
        first_answer = calculation_function(first_number, second_number)

        print(f"{first_number} {pick_operation} {second_number} = {first_answer}")

        if input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.: ") == "y":
            first_number = first_answer
        else:
            calculate = False
            exit()

calculator()
# operation_symbol = input("Pick another operation: ")
# third_number = int(input("What's the next number?: "))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(first_answer, third_number)

# print(f"{first_answer} {operation_symbol} {third_number} = {second_answer}")