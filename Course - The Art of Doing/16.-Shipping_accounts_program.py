#usr/bin/env python3

# Getting username and greeting user
username = input("Welcome to the Shipping Accounts Program\n\nHello, what is your username? ").title().strip()
print(f"\nHello {username}. Welcome back to your account.\nCurrent shipping prices are as follows:\n\nShipping orders 0 to 99:\t\t$5.10 each\nShipping orders 100 to 499:\t\t$5.00 each\nShipping orders 500 to 999:\t\t$4.95 each\nShipping orders over 1000:\t\t$4.80 each\n\n")

# Asking how many items and calculating how much would it cost
items = int(input("How many items would you like to ship? "))
while True:
    if items > 0:
        if items <= 100:
            print(f"To ship {items} items it will cost you $" + str(round((items * 5.10), 2)) + " at $5.10 per item\n")
            break
        elif items <= 499:
            print(f"To ship {items} items it will cost you $" + str(round((items * 5.00), 2)) + " at $5.00 per item\n")
            break
        elif items <= 999:
            print(f"To ship {items} items it will cost you $" + str(round((items * 4.95), 2)) + " at $4.95 per item\n")
            break
        else:
            print(f"To ship {items} items it will cost you $" + str(round((items * 4.80), 2)) + " at $4.80 per item\n")
            break
    else: 
        print("Wrong quantity, pal. Try again.")
        continue

# Checking whether or not the user wants to proceed
choice = input("Would you like to place this order? (y/n): ")
if choice == "y":
    print(f"Okay. Shipping your {items} items.")
else:
    print(f"Okay, no order is being placed at this time.")