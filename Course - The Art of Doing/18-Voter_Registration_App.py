#!/usr/bin/env python3

# Initializing
name = input('Welcome to the Voter Registration App\n\nPlease enter your name: ').title().strip()
age = int(input('Please enter your age: '))
parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]

# If the user is above 18, they can register to vote and the program starts
if age > 17:
    print('Congratulations! You are old enough to register to vote.\n\nHere is a list of political parties to join:')
    for party in parties: 
        print(f"\t- {party}")
    party_choice = input('What party would you like to join: ').strip().title() # User choses a party
    if party_choice in parties: # if - in - condition
        print(f'Congratulations {name}! You have joined the {party_choice} party!') 
        if party_choice.startswith("R") or party_choice.startswith("D"): # Filtering with .startswith()
            print("That is a major party.")
        elif chosenparty.startswith('I'):
            print('You ')
        else:
            print('That is a not major party.')
    else:
        print("Sorry this is not a given party.")
else:
    print(f'Sorry {name}, you are not enough to vote. Come back when you are 18')