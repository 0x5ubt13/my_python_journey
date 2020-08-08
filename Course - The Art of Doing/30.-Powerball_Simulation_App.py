#!/usr/bin/python3
from random import randint
chance = 1
my_numbers = []
x = 0

# while loop for making the whole simulation reiterable
while True:
    # Greeting and getting initial input from user
    print("-"*10 + " Power-Ball Simulator " + "-"*10)
    white_balls = int(input("How many white-balls to draw from for the 5 winning numbers (normally 69)? "))
    if white_balls < 5:
        white_balls = 5
    red_balls = int(input("How many red-balls to draw from for the Power-Ball (normally 26)? "))
    if red_balls < 1:
        red_balls = 1
    # For loop to get the odds
    for n in range(6, 1, -1):
        chance *= white_balls
        white_balls -= 1
    chance *= red_balls
    chance /= 120
    print(f"You have a 1 in {chance} chance of winning this lottery.")

    # defining win function to randomise the winning numbers and put them in a list
    def win():
        #print("Starting win()")  # Uncomment this line for debugging purposes
        global winning_numbers
        global white_balls
        global red_balls
        global printable_winning_numbers
        winning_numbers = []
        printable_winning_numbers = ''
        while len(winning_numbers) < 5:
            new_number = randint(1, white_balls)
            if new_number not in winning_numbers:
                winning_numbers.append(new_number)
        winning_numbers.sort()
        new_red_ball_number = randint(1, red_balls)
        winning_numbers.append(new_red_ball_number)
        for i in winning_numbers:
            printable_winning_numbers += " " + str(i)
        printable_winning_numbers = printable_winning_numbers.strip()
        #print("Done!")      # Uncomment this line for debugging purposes
    # Defining random tickets generator
    def my_num():
        global my_numbers
        my_numbers = []
        while len(my_numbers) < 5:
            new_number = randint(1, white_balls)
            if new_number not in my_numbers:
                my_numbers.append(new_number)
        if len(my_numbers) == 5:
            my_new_red_ball_number = randint(1, red_balls)
            my_numbers.sort()
            my_numbers.append(my_new_red_ball_number)
        print(my_numbers)

    # Make user input in what interval they want to buy tickets and start the lottery game
    interval = int(input("Purchase tickets in what interval? "))
    win()
    print("-"*10 + " Welcome to the Power-Ball " + "-"*10)
    print(f"Tonight's winning numbers are: {printable_winning_numbers}")
    input("Press enter to begin purchasing tickets!!! ")
    while my_numbers != winning_numbers:
        if x > 1:
            keep_betting = input(f"{x} tickets purchased so far with no winners...\n\nKeep purchasing tickets? (y/n) ").lower().strip()
            if keep_betting == 'y' or keep_betting == 'yes':
                pass
            else:
                break 
        # Start buying tickets
        for i in range(interval):
            x += 1
            if my_numbers != winning_numbers:
                my_num()
            else:
                break
    # If the loop is broken by either the user being tired of playing or because they won, this code is executed next
    if my_numbers == winning_numbers:
        print(f"You won!\nYour numbers combination {my_numbers} have won the lottery!!!")
        print(f"You needed to buy {x} tickets in order to win!!")
    else:
        print(f"You bought {x} tickets and still lost!\nBetter luck next time!")
        break
    
    #Play again?
    while True: # Yet another while loop in order to make sure user inputs a correct answer
        again = input("Do you want to play again? (y/n) ").lower().strip()
        if again == 'n' or again == 'no':
            break
        elif again.startswith("n") and len(again) >= 3: 
            break
        elif again == 'y' or again == 'yes':
            break
        else:
            continue
    if again == 'n' or again == 'no': # :( bye!
        print("Thanks for using the Power-ball Simulator!! Goodbye!!")
        break
    elif again.startswith("n") and len(again) >= 3: 
        print("You haven't given a proper 'no' or 'n' response therefore the game will restart")
    elif again == 'y' or again == 'yes':
        print("Amazing!")
        continue




