#!/usr/bin/python3

savings = 0
checking = 0

def creating_acc():
    global name
    global savings_account
    global checking_account
    print("Welcome to the Python First National Bank\n")
    name = input("Hello, what is your name? ").title().strip()
    savings_account = int(input("How much money would you like to set up your savings account with: "))
    checking_account = int(input("How much money would you like to set up your checking account with: "))

def info():
    print(f"Current Account Information\nName: {name}\nSavings: £{savings_account}\nChecking: £{checking_account}")


#which account / if account type doesnt exist, promt it
#deposit or withdrawal / if balance -0, not able to withdraw
#how much
#show acc info


