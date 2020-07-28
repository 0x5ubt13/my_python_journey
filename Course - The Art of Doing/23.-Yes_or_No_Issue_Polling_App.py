#!/usr/bin python3

voters = {}
nay = 0
yay = 0
counter = 0
counter_names = []

print("Welcome to the Yes or No Issue Polling App!")
issue = input("What is the yes or no issue you will be voting on today: ")
votes = int(input("What is the number of voters you will allow on the issue: "))
password = input("Enter a password for polling results: ")

for vote in range(votes):
    while True:
        voter = input("\nPlease enter your full name: ")
        if voter in voters.keys(): 
            print("Sorry, it seems that someone with that name has already voted")
            continue
        else:    
            vote = input("Here is our issue: " + issue + "\nWhat do you think...? Yes or no? ").lower().strip()
            voters[voter] = vote
            if vote == 'yes' or vote == 'y':
                yay += 1
            elif vote == 'no' or vote == 'n':
                nay += 1
            else:
                print("That is not a yes or no answer, but whatever...")
            print("Thank you " + voter + "!. Your vote of " + vote + " has been recorded.\n")
            break


for k in voters.keys():
    counter += 1
    counter_names.append(k)

print("The following " + str(counter) + " people voted: ")
for i in range(len(counter_names)):
    print(counter_names[i])

print("On the following issue: " + issue)
if yay > nay:
    print("\nYes wins! " + str(yay) + " votes to " + str(nay), end='.\n')
elif nay > yay:
    print("\nYes wins! " + str(nay) + " votes to " + str(yay), end='.\n')
elif nay == yay:
    print("\nIt's a tie!!")

password_check = input("To see the voting results enter the admin password: ")
if password_check == password:
    for key, val in voters.items():
        print("Voter: " + key + "\t\tVote: " + val)
else:
    pass
print("Thank you for using the Yes or No Issue Polling App.")
