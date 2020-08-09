#!/usr/bin/python3.

history = []

def addition(number1, number2):
    """ Sums and records the operation in history[] """
    result = number1 + number2
    print(f"The sum of {number_1} and {number_2} is {result}")
    history.append(f"{number_1} + {number_2} = {result}")
    return result 

def subtraction(number1, number2):
    """ Subtracts and records the operation in history[] """
    result = number1 - number2
    print(f"The difference of {number_1} and {number_2} is {result}")
    history.append(f"{number_1} - {number_2} = {result}")
    return result 

def multiplication(number1, number2):
    """ Multiplies and records the operation in history[] """
    result = number1 * number2
    print(f"The product of {number_1} and {number_2} is {result}")
    history.append(f"{number_1} * {number_2} = {result}")
    return result 

def division(number1, number2):
    """ Divides and records the operation in history[] """
    result = number1 / number2
    print(f"The quotient of {number_1} and {number_2} is {result}")
    history.append(f"{number_1} / {number_2} = {result}")
    return result

def exponentiation(number1, number2):
    """ Raises number1 to the power of number2 and records the operation in history[] """
    result = number1 ** number2
    print(f"The result of {number_1} raised to the {number_2} power is {result}")
    history.append(f"{number_1} ** {number_2} = {result}")
    return result 

def again():
    """ Code to make the program loopable """
    again = input("Would you like to run the program again (y/n): ").lower().strip()
    if again == "n":
        run = False
    else:
        run = True    
    return run

def user_input():
    """ Takes user input and chooses the right function """
    global number_1
    global number_2
    global operation
    number_1 = int(input("Please enter a number: "))
    number_2 = int(input("Please enter a number: "))
    while True:
        operation = input("Enter an operation (addition, subtraction, multiplication, division, or exponentiation): ").lower().strip()
        if operation == 'a' or operation == 'addition':
            addition(number_1, number_2)
        elif operation == 's' or operation == 'subtraction':
            subtraction(number_1, number_2)
        elif operation == 'm' or operation == 'multiplication':
            multiplication(number_1, number_2)
        elif operation == 'd' or operation == 'division':
            division(number_1, number_2)
        elif operation == 'e' or operation == 'exponentiation':
            exponentiation(number_1, number_2)
        else:
            print("Operation not valid, please try again")
            continue
        break

def summary():
    """ Prints out the summary """
    print("Calculation summary:")
    for i in history:
        print(i)
    print("Thank you for using the Python Calculator App. Goodbye!")


# Main code
running = True
while running:
    print("Welcome to the Python Calculator App!\nEnter two numbers and an operation and the desired operation will be performed")
    user_input()
    running = again()
summary()

