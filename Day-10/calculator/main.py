#Write a Python calculator that can perform: addition, subtraction, division, multiplication and modulus operations. 

#It should accept user input
import os
from art import logo
from subtract import subtract
from add import add
from divide import divide
from multiply import multiply
from modulus import modulus
clear = lambda: os.system('cls')
print("Welcome to Zuri Calculator!")

operations = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply,
    '%': modulus,
} 

def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("Enter the next number: "))

        calculation_function = operations[operation_symbol]

        result = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result} ")

        if (input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. :  ").lower()) == 'y':
            num1 = result

        else:
            should_continue = False
            clear()
            calculator()

calculator()