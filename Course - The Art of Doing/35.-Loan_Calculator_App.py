#!/usr/bin/python3
from matplotlib import pyplot as plt

# Vars
x = 0
plot = []
paid = 0
interest_paid = 0
loan = int(input("Please enter the amount of Loan you want to borrow: "))
interest = float(input("Please enter the intrest rate: "))
m_interest = (interest / 100) / 12 
monthly_payment = int(input("Please enter the desired monthly payment: "))
pending = loan

# Main code
debt = True
while debt: 
    print(f"""
    ---- Loan information after {x} months: ----
    Principal: £{pending:0.2f}
    Rate: {interest}%
    Monthly payment: {monthly_payment}
    Money Paid: £{paid}""")
    x += 1 
    c_interest = pending * m_interest
    interest_paid += c_interest
    if pending >= (monthly_payment - c_interest):
        pending -= (monthly_payment - c_interest)
        paid += monthly_payment
    else:
        paid += pending
        pending -= pending
    plot.append(pending)        
    if pending <= 0:
        debt = False
    elif pending >= loan:
        print("You will NEVER pay off your loan!!!\nYou cannot get ahead of the interest! :-(")
        debt = False
print(f"""\n\nCongratulations! You paid your loan in {x} months!!
You paid £{paid:0.2f} in total and {interest_paid:0.2f} in interests!""")

# Creating the plot chart
if pending == 0:
    plt.plot(plot)
    plt.title(f"{interest}% interest rate with £{monthly_payment} monthly payment")
    plt.ylabel("Principal of Loan")
    plt.xlabel("Number of Months")
    plt.show()