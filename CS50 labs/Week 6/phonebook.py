import csv

# # Version 1:
# people = {
#     "Carter": "+1-617-495-1000",
#     "David": "+1-949-468-2750",
# }

# name = input("Name to look up: ").title()

# # Linear search
# if name in people:
#     print(f"{name}'s number: {people[name]}")
# else:
#     print(f"Sorry, {name} is not in the phonebook")

# Version 2:
name = input("Name: ").title()
number = input("Number: ")

with open("./phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, number])
