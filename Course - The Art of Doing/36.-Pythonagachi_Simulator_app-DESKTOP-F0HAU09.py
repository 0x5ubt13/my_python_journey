#!/usr/bin/python3
import random

class Tamagotchi():
    """ Class to simulate a tamagotchi """
    
    def __init__(self, name, difficulty=3):
        """ Initializing attributes """
        self.name = name.title() 
        self.difficulty = 0
        
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0
        self.food_inventory = 2
        self.is_awake = True
        self.is_alive = True
        self.turns_alive = 0

    def display_info(self):
        """ Display info on the tamagotchi """
        print(f"-= Pet: {self.name} =-")
        print("Hunger (1-10): " + str(self.hunger))
        print("Boredom (1-10): " + str(self.boredom))
        print("Tiredness (1-10): " + str(self.tiredness))
        print("Dirtiness (1-10): " + str(self.dirtiness))
        print("\nFood Inventory " + str(self.food_inventory) + " pieces")
        if self.is_awake:
            print("Current status: Awake")
        else:
            print('Current status: Sleeping')
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
        print(f"-= Pet: {self.name} =-")
        print("Hunger (1-10): " + str(self.hunger))
        print("Boredom (1-10): " + str(self.boredom))
        print("Tiredness (1-10): " + str(self.tiredness))
        print("Dirtiness (1-10): " + str(self.dirtiness))
        print("\nFood Inventory " + str(self.food_inventory) + " pieces")
        if self.is_awake:
            print("Current status: Awake")
        else:
            print('Current status: Sleeping')
        input("\n\nPress (enter) to continue...")

    def eat(self):
        """ make the tamagotchi eat """
        self.hunger -= random.randint(1, difficulty)
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
        print(f"{self.name} has fallen sleep. ZZZzzzzZZZZzzz")
    

    def clean(self):
        """ make the tamagotchi take a bath """
        self.dirtiness = 0
        print(f"{self.name} has had a bath. All clean and smelling good!!")
    

    def food(self):
        """ make the tamagotchi go out for food """
        new_pieces = random.randint(1,3)
        self.food_inventory += new_pieces
        print(f"{self.name} has gone out looking for food and found {new_pieces}")


    def alive(self):
        """ checks whether the tamagotchi is alive or not """
        if self.hunger == 10 or self.dirtiness == 10:
            self.is_alive = False
            if self.hunger == 10:
                print(f'{self.name} has starved')
            elif self.dirtiness == 10:
                print(f"{self.name} has suffered an infection and died...")
        else:
            pass
        

    def adding_turn(self):
        """ loops through a new turn """
        self.turns_alive += 1
        self.hunger += random.randint(0, difficulty)
        if self.hunger > 10:
            self.hunger = 10
        self.boredom += random.randint(0, difficulty)
        if self.boredom > 10:
            self.boredom = 10
        self.tiredness += random.randint(0, difficulty)
        if self.tiredness > 10:
            self.tiredness = 10
        self.dirtiness += random.randint(0, difficulty)
        if self.dirtiness > 10:
            self.dirtiness = 10

    def turn(self):
        if self.turns_alive >= 1:   
            self.alive()
            if self.is_alive == False:
                print(f"R.I.P.\n\nWell done, your pet {self.name} survived for {self.turns_alive} turns")        
            else:
                if self.is_awake == False:
                    while True:
                        awake_him = int(input(f"Press (6) to try and wake {self.name} up: "))
                        if awake_him == 6:
                            wake_up = random.randint(0, difficulty)
                            if wake_up == difficulty:
                                self.is_awake = True
                            else:
                                print(f"{self.name} won't wake up...")
                                print("ZZZZzzzzzzz.... ZZZzzzzz... ZZZZZZZZzzzzzzzzzzz....")
                            break
                        else:
                            print("Incorrect number. Try again")
                else:
                    if self.boredom == 10:
                        self.sleep()
                    else:
                        choice = int(input("What's your choice? "))
                        while True:
                            if choice in range(1, 6):
                                if choice == 1:
                                    self.eat()
                                elif choice == 2:
                                    self.amuse()
                                elif choice == 3:
                                    self.sleep()
                                elif choice == 4:
                                    self.clean()
                                elif choice == 5:
                                    self.food()
                                break
                            else:
                                print("Incorrect key. Try again")
        else:
            pass

round_number = 0
playing = True
alive = True
while playing:
    difficulty = int(input("Please enter the desired level of difficulty (1-5): "))
    name = input("What's your new pet's name? ")
    pet = Tamagotchi(name, difficulty)
    while alive:
        if round_number >= 1:
            print(f"------ Round #{round_number} ------")
            pet.display_info()
            pet.turn()
            if pet.is_alive == False:
                alive = False
                break
        print(f"------ Round #{round_number} summary ------")
        round_number += 1
        pet.adding_turn()
        pet.summary()

    again = input("Play again? (y/n): ")
    if again == 'n':
        print("Thanks for using my Python Tamagotchi App!! Have a good one!")
        playing = False    







    
        