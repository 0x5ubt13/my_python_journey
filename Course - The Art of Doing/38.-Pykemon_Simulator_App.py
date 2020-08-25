#!/bin/env/python3
import random

class Pykemon():
    """ Class to define the Pykemons """

    def __init__(self):
        """ Initialising Pykemon() with basic attributes """

        self.health = 0
        self.element_types = ["FIRE", "WATER", "GRASS"]
        self.speed = 0
        self.attacks = {
            "physical":["Scratch", "Bite", "Vine Whip"],
            "risky":["Ember", "Slash", "Wrap"],
            "restorative":["Light", "Dive", "Grow"],
            "elemental":["Fire blast", "Water Cannon", "Leaf Blade"],
        }
        self.name = ""
        self.random_type = ""
        self.names = ["Spatol", "Zantbat", "Chewdie", "Abbacab", "Swagilybo"]


    def attacks_stats_and_descriptions(self, kind="rand"):
        """ Getting the attacks and stats for the pykemons and coding the descriptions """
        
        if kind == "fire":
            self.random_type = self.element_types[0]
        elif kind == "water":
            self.random_type = self.element_types[1]
        elif kind == "grass":
            self.random_type = self.element_types[2]
        elif kind == "rand":
            self.random_type = self.element_types[random.randint(0,2)]

        self.health = random.randint(79, 99)
        self.speed = random.randint(5, 10)
        
        self.physical_attack_definition = "\t\tAn efficient attack...\n\t\tGuaranteed to do damage within the range of 15 to 25 damage points."
        self.risky_attack_definition = "\t\tA risky attack...\n\t\tCould deal up to 50 damage points or as little as 0 damage points"
        self.restorative_attack_definition = "\t\tA restorative move...\n\t\tGuaranteed to heal your Pykemon 15 to 25 health points"

        if self.random_type == self.element_types[0]: # Fire
            self.physical_attack = self.attacks["physical"][0]
            self.risky_attack = self.attacks["risky"][0]
            self.restorative_attack = self.attacks["restorative"][0]
            self.elemental_attack = self.attacks["elemental"][0]
            self.elemental_attack_definition = "A powerful FIRE based attack...\n\t\tGuaranteed to deal MASSIVE damage to GRASS type Pykemon"

        elif self.random_type == self.element_types[1]: # Water
            self.physical_attack = self.attacks["physical"][1]
            self.risky_attack = self.attacks["risky"][1]
            self.restorative_attack = self.attacks["restorative"][1]
            self.elemental_attack = self.attacks["elemental"][1]
            self.elemental_attack_definition = "A powerful WATER based attack...\n\t\tGuaranteed to deal MASSIVE damage to FIRE type Pykemon"

        elif self.random_type == self.element_types[2]: # Grass
            self.physical_attack = self.attacks["physical"][2]
            self.risky_attack = self.attacks["risky"][2]
            self.restorative_attack = self.attacks["restorative"][2]
            self.elemental_attack = self.attacks["elemental"][2]
            self.elemental_attack_definition = "A powerful GRASS based attack...\n\t\tGuaranteed to deal MASSIVE damage to WATER type Pykemon"


    def new_pykemon_def(self, name, element, health, speed):
        """ Prints all the info for a new Pykemon """

        print(f"""  
        Name: {name}
        Element Type: {element}
        Health: {health}/{health}
        Speed: {speed}
        
        """)


    def choosing(self):
        """ Makes the player choose a Pykemon to play with """

        for element in self.element_types:
            name = random.choice(self.names)
            self.attacks_stats_and_descriptions(element.lower())
            self.new_pykemon_def(name, element, self.health, self.speed)  


    def battle(self):
        """ Simulates a battle between 2 Pykemon """

        



print("""
Welcome to Pykemon!

Can you become the world's greatest Pykemon Trainer???

Don't worry! Prof 5ubt13 is here to help you on your quest.
He would like to gift you your first Pykemon!

Here are three potential Pykemon partners:
""")

input("Press (enter) to choose your Pykemon!")
game = Pykemon()
game.choosing()
























