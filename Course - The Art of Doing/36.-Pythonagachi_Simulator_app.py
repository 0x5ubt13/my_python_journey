#!/usr/bin/python3
import random

class Tamagotchi():
    """ Class to simulate a tamagotchi """
    
    def __init__(self, name, hunger, boredom, tiredness, dirtiness, food_inventory, awake):
        """ Initializing attributes """
        self.name = name.title()
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0
        self.food_inventory = 0
        self.is_awake = awake #boolean

        self.is_alive = True
        self.turns_alive = 0

    def display_info(self):
        """ Display info on the tamagotchi """
        print("Hunger (1-10):\t" + str(self.hunger))
        print("Boredom (1-10):\t" + str(self.boredom))
        print("Tiredness (1-10):\t" + str(self.year_built))
        print("Dirtiness (1-10):\t" + str(self.price))
        print("\nFood Inventory " + str(self.food_inventory) + " pieces")
        print("Current status: " + str(self.awake))
        print("""
                       Menu:
            ~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~~  1.- Eat             ~~
            ~~  2.- Play            ~~
            ~~  3.- Sleep           ~~
            ~~  4.- Take a bath     ~~
            ~~  5.- Forage for food ~~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)

    def summary(self):
        """ Display info on the tamagotchi after the round"""
        print("Hunger (1-10):\t" + str(self.hunger))
        print("Boredom (1-10):\t" + str(self.boredom))
        print("Tiredness (1-10):\t" + str(self.year_built))
        print("Dirtiness (1-10):\t" + str(self.price))
        print("\nFood Inventory " + str(self.food_inventory) + " pieces")
        print("Current status: " + str(self.awake))
        input("\n\nPress (enter) to continue...")

    def eat(self):
        """ make the tamagotchi eat """
        self.hunger -= random.randint(1, 3)
        self.food_inventory -= 1
        print(f"Yummm!! {self.name} ate a great meal!")

    def amuse(self):
        """ make the tamagotchi play """
        self.boredom -= random.randint(1, 3)
        print(f"{self.name} wants to play a game")
        print(f"{self.name} is thinking of a number: 1, 2 or 3")
        guess = int(input('What is your guess? '))
        to_guess = random.randint(1, 3)
        if guess == to_guess:
            print("CORRECT! You guessed the number!")
        else:
            print(f"WRONG! {self.name} was thinking of {to_guess}")
        
    
    def sleep(self):
        """ make the tamagotchi sleep """
        self.tiredness = 0
        self.is_awake = False
    
    def clean(self):
        """ make the tamagotchi take a bath """
        self.dirtiness = 0
    
    def food(self):
        """ make the tamagotchi go out for food """
        
    def alive(self):
        """ checks whether the tamagotchi is alive or not """

    def turn(self):
        """ loops through a new turn """
        self.turns_alive += 1
        self.hunger += random.randint(0, 3)
        self.boredom += random.randint(0, 3)
        self.tiredness += random.randint(0, 3)
        self.dirtiness += random.randint(0, 3)
        