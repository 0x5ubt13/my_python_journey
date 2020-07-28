#!/usr/bin/env python3
from random import randint

# Initializing vars and list 
turn = 0
p_score = 0
c_score = 0
choices = ['Rock', 'Scissors', 'Paper']

# Functions
def score(): 
    print(f"Round {turn}\nPlayer {p_score}\tComputer {c_score}")

def game():
    global p_score, c_score # To avoid UnboundLocalError
    c_index = randint(0, 2) # Randomising computer's choice
    c_choice = choices[c_index]
    print(f"\tComputer: {c_choice}\n\tPlayer: {p_choice}")
    if c_choice == p_choice:
        print("\tIt is a tie, how boring!\nThis round is a tie.\n")
    elif c_choice == choices[0] and p_choice == choices[1]:
        print(f"\tRock smashes Scissors!\n\tComputer wins round {turn}")
        c_score += 1
    elif c_choice == choices[0] and p_choice == choices[2]:
        print(f"\tPaper covers Rock!\n\tPlayer wins round {turn}")
        p_score += 1
    elif c_choice == choices[1] and p_choice == choices[0]:
        print(f"\tRock smashes Scissors!\n\tPlayer wins round {turn}")
        p_score += 1
    elif c_choice == choices[1] and p_choice == choices[2]:
        print(f"\tScissors cut Paper!\n\tComputer wins round {turn}")
        c_score += 1
    elif c_choice == choices[2] and p_choice == choices[0]:
        print(f"\tPaper covers Rock!\n\tComputer wins round {turn}")
        c_score += 1
    elif c_choice == choices[2] and p_choice == choices[1]:
        print(f"\tScissors cut Paper!\n\tPlayer wins round {turn}")
        p_score += 1
    else:
        print("Error")
        
def final_result():
    print(f"Final game results:\n\tRounds played: {turn}\n\tPlayer score: {p_score}\n\tComputer score: {c_score}")
    if p_score < c_score:
        print("Winner: Computer :-(")
    elif p_score > c_score:
        print("Winner: Player! Well done! :-)")
    elif p_score == c_score:
        print("Winner: Tie. Play again!")

# Number of rounds and main game loop
rounds = int(input("Welcome to a game of Rock, Paper, Scissors!\n\nHow many rounds would you like to play? "))
for r in range(rounds):
    turn += 1
    score()
    p_choice = input("Time to pick... Rock, Paper, Scissors: ").strip().title()
    game()
    
# Print result
final_result()




