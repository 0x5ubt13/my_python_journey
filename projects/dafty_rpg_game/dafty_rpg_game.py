#!/bin/env/python3

# Turn based RPG Style Example

import random

# Parent Class
class Game():
    """ Making this lab a bit more fun to code and a bit more functional """

    def __init__(self):
        """ Initialising class"""

    def attack(self, attacker, enemy):
        """ A normal attack dealing physical damage """

        # define a function to generate a number between 1 and 20
        damage = random.randint(1, 20)

        # 1) Create a print statement that prints out the enemy attack variable
        print(f"{attacker.name} attacks. Deals {damage} damage to {enemy.name}.")
        enemy.attributes["Current health"] -= damage

    
    def fire(self, caster, enemy):
        """ Attack which does 10% of the enemys health but costs 5 magic points from the attacker """

        print(f"{caster.name} casts a fireball. Deals 10% to the maximum {enemy.name}'s health.")

        caster.attributes["Current magic"] -= 5
        enemy.attributes["Current health"] -= 0.1 * enemy.attributes["Max health"]


    def random_attack(self, attacker, enemy):
        """ Randomises the use of either attack() or fire() to keep the game interesting """

        odds = random.randint(0, 1)

        if odds == 0:
            return self.attack(attacker, enemy)
        else:
            return self.fire(attacker, enemy)


    def show_stats(self, character):
        """ Display the current stats """

        print(character.attributes, "\n")


# Child Class
class Character():
    """ Our main character with copyright """
    
    def __init__(self, name, health, magic):
        """ Initialising attributes of players"""
        
        self.name = name
        self.current_health = health,
        self.max_health = health,
        self.current_magic = magic,
        self.max_magic = magic,


        # create two characters with attributes in dictionary
        self.attributes = {
            "Name": name.title(),
            "Current health": health,
            "Max health": health,
            "Current magic": magic,
            "Max magic": magic, 
        }

        self.is_alive = True


    def die(self):
        """ If you run out of health, you die """

        if self.attributes["Current health"] <= 0:
            self.is_alive = False
            print(f"\nCharacter {self.name} has died at turn number {turns_counter}")
            input("\nPress (Enter) to continue")



# Main code
print("""
You will find some similarities with real turn-based RPGs from the 90's.
Please, don't report us! This is only for academic purposes!

Enjoy!!
\n\n""")

playing_main = True
while playing_main:
    turns_counter = 0

    game = Game()
    
    player = Character("Cloud", 100, 50)
    enemy = Character("Enemy", 110, 40)

    while player.is_alive and enemy.is_alive:

        print("---------- Turn number", turns_counter, "----------\n")

        game.random_attack(player, enemy)
        game.show_stats(enemy)
        enemy.die()
               
        game.random_attack(enemy, player)
        game.show_stats(player)
        player.die()

        turns_counter += 1

    again = input("Play again? (y/n): ").strip().lower()
    if again.startswith("y"):
        continue
    else:
        break
