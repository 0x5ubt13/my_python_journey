#!/usr/bin/python3

savings = 0
checking = 0

def creating_acc():
    """code for creating the app based on user input"""
    global name
    global savings
    global checking
    if name.isalpha():
        print(f"Welcome back, {name}")
    savings_account = int(input("How much money would you like to set up your savings account with: "))
    savings += savings_account
    checking_account = int(input("How much money would you like to set up your checking account with: "))
    checking += checking_account

def info():
    """print the account info"""
    print(f"Current Account Information\nName: {name}\nSavings: £{savings}\nChecking: £{checking}")

def selection():
    """select what the user wants to do"""
    global acc_selection
    global transaction_selection
    global how_much
    while True:
        acc_selection = input("Which account do you like to access (Savings or Checking?) ").lower().strip()
        if acc_selection != "savings" and acc_selection != "checking":
            print("Sorry, we cannot do that for you today")
            continue
        else:
            break
    transaction_selection = input("What type of transaction would you like to make? (Deposit or Withdrawal?) ").lower().strip()
    how_much = int(input("How much money? "))

def operation():
    global savings
    global checking
    """executes user operation"""
    if acc_selection == "savings":
        if transaction_selection == "deposit":
            savings += how_much
            print(f"Successfully deposited £{how_much} into {name}'s {acc_selection} account")
        elif transaction_selection == "withdrawal":
            if savings < how_much:
                print(f"Sorry, by withdrawing £{how_much} your account would be in credit.")
            else:
                savings -= how_much
    elif acc_selection == "checking":
        if transaction_selection == "deposit":
            checking += how_much
            print(f"Successfully deposited £{how_much} into {name}'s {acc_selection} account'")
        elif transaction_selection == "withdrawal":
            if checking < how_much:
                print(f"Sorry, by withdrawing £{how_much} your account would be in credit.")
            else:
                checking -= how_much

def again():
    global running
    again = input("Would you like to make another transaction? (y/n) ").lower().strip()
    if again == 'n':
        running = False
        print("Have a nice day!")

# Main code
running = True
print("Welcome to the Python First National Bank\n")
name = input("Hello, what is your name? ").title().strip()
while running:
    creating_acc()
    info()
    selection()
    operation()
    info()
    again()
