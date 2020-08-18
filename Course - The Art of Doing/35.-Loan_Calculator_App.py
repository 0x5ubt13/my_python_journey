#!/usr/bin/python3
import matplotlib

x = 0
paid = 0
interest_paid = 0
loan = int(input("Please enter the amount of Loan you want to borrow: "))
interest = float(input("Please enter the intrest rate you want to pay each month: "))
m_interest = (interest / 100) / 12 
monthly = int(input("Please enter the desired monthly payment: "))
principal = loan
    

debt = True
while debt: 
    print(f"---- Loan information after {x} months: ----\nPrincipal: {principal:0.2f}\nRate: {interest}\nMonthly payment: {monthly}\nMoney Paid: {paid}")
    x += 1
    paid += monthly 
    c_interest = loan * m_interest
    interest_paid += c_interest
    loan_left = loan - paid
    principal = ((loan - paid) * m_interest) + loan_left  







    
    if principal <= 0:
        debt = False