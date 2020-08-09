#!/usr/bin/python3
from random import randint

playing = True
while playing:
    
    rolls = []

    def roll(number_of_sides):
        """ rolling the dice of X sides """
        random_roll = randint(1, number_of_sides)
        rolls.append(random_roll)
        print("\t\t", random_roll)

    def rolls_sum():
        """ sums all rolls """ 
        total_sum = 0
        for i in rolls:
            total_sum += i
        return total_sum  

    print("Welcome to the Python Dice App")

    sides = int(input("How many sides would you like on your dice? "))
    dice = int(input("How many dice would you like to roll? "))

    print(f"You rolled {dice} {sides} sided dice.")

    print("-" * 10 + " Results are as follows " + "-" * 10)
    for i in range(dice):
        roll(sides)

    total = rolls_sum()
    print(f"The total value of your roll is {total}")

    again = input("\nWould you like to roll again? (y/n) ").lower().strip()
    if again == 'n':
        playing = False
        print("Thanks for using my App! Bye!")
