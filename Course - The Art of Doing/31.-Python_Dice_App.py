#!/usr/bin/python3
from random import randint

def roll(number_of_sides):
    """ rolling the dice of X sides """
    random = randint(1, number_of_sides)
    



print("Welcome to the Python Dice App")

sides = int(input("How many sides would you like on your dice? "))
dice = int(input("How many dice would you like to roll? "))

print(f"You rolled {dice} {sides} sided dice.")

print("-" * 10 + " Results are as follows " + "-" * 10)

print(f"The total value of your roll is {total_value}")