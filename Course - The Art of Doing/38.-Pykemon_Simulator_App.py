#!/bin/env/python3
import random


# Parent class
class Pykemon():
    """ A model of a generic Pykemon character """

    def __init__(self, name, element, health, speed):
        """ Initialise attributes """
        self.name = name.title()
        self.element = element
        # Current health is current, max health will be referenced for healing
        self.current_health = health
        self.max_health = health
        self.speed = speed
        self.is_alive = True
    
    def light_attack(self, enemy):
        """ A light attack guaranteed to do minimal damage """
        damage = random.randint(15,25)
        
        # All Pykemon will have a list moves = [light, heavy, restore, special]
        # All light attacks will appear at index 0 in the list moves
        # This attribute will be initialized in the child class
        print(f"Pykemon {self.name} used {self.moves[0]}")
        print(f"It dealt {damage} damage.")
        
        # Deal damage to the enemy
        enemy.current_health -= damage

    
    def heavy_attack(self, enemy):
        """ A heavy attack that could deal MASSIVE damage, or no damage at all """
        damage = random.randint(0,50)

        # All Pykemon will have a list moves = [light, heavy, restore, special]
        # All heavy attacks will appear at index 1 in the list moves
        # This attribute will be initialized in the child class
        print(f"Pykemon {self.name} used {self.moves[1]}")

        # Dealt no damage
        if damage < 35:
            print("The attack missed!!!")
        else:
            print(f"It dealt {damage} damage.")

            # Deal the damage to the enemy
            enemy.current_health -= damage


    def restore(self):
        """ Healing move that will restore our current health """

        # Generate a restore value
        heal = random.randint(15, 25)

        # All Pykemon will have a list moves = [light, heavy, restore, special]
        # All restore moves will appear at index 2 in the list moves
        # This attribute will be initialized in the child class
        print(f"Pykemon {self.name} used {self.moves[3]}")
        print(f"It healed {heal} health points")
        
        # Heal the Pykemon
        self.current_health += heal

        # Check to see if we have exceeded the max health of the Pykemon
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def faint(self):
        """ If you run out of health, you faint... """

        if self.current_health <= 0:
            self.is_alive = False
            print(f"Pykemon {self.name} has fainted")
            input("Press (Enter) to continue")


    def show_stats(self):
        """ Display the current stats """
        
        print(f"""  
        Name: {self.name}
        Element Type: {self.element}
        Health: {self.current_health} / {self.max_health}
        Speed: {self.speed}
        \n""")

# Child Classes
class Fire(Pykemon):
    """ A Fire based Pykemon that is a child of the Pykemon class. """

    def __init__(self, name, element, health, speed):
        """ Initialise attributes from the parent Pykemon class."""
        super().__init__(self, name, element, health, speed)
        # Move list unique to all Fire type Pykemon
        moves = ["Scratch", "Ember", "Light", "Fire Blast"]


    def special_attack(self, enemy):
        """FIRE BLAST: an elemental fire move. Massive dmg to Grass type, 
        normal dmg to Fire type, minimal dmg to Water type. """

    print(f"Pykemon {self.name} used {self.moves[3]}!")

    # Generate damage based on enemy type:
    if enemy.element == "grass":
        print("It's SUPER effective!")
        damage = random.randint(35, 50)
    elif enemy.element == "water":
        print("It's not very effective...")
        damage = random.randint(5, 10)
    else:
        damage = random.randint(10, 30)

    # Deal damage
    print(f"It dealt {damage} damage,")
    enemy.current_health -= damage

    
    def move_info(self):
        """ Display pykemon move info """
        print(f"\n{self.name} Moves:")
        
        # Light
        print(f"-- {self.moves[0]} --")
        print("\tAn efficient attack...\n\tGuaranteed to do damage within the range of 15 to 25 damage points.\n")
        # Heavy attack
        print(f"-- {self.moves[1]} --")
        print("\tA risky attack...\n\tCould deal up to 50 damage points or as little as 0 damage points\n")
        # Restorative move
        print(f"-- {self.moves[2]} --")
        print("\tA restorative move...\n\tGuaranteed to heal your Pykemon 15 to 25 health points\n")
        # Elemental attack
        print(f"-- {self.moves[3]} --")
        print("\tA powerful FIRE based attack...\n\tGuaranteed to deal MASSIVE damage to GRASS type Pykemon\n")



class Water(Pykemon):
    """ A Water based Pykemon that is a child of the Pykemon class. """

    def __init__(self, name, element, health, speed):
        """ Initialise attributes from the parent Pykemon class."""
        super().__init__(self, name, element, health, speed)
        # Move list unique to all Water type Pykemon
        moves = ["Bite", "Splash", "Dive", "Water Cannon"]


    def special_attack(self, enemy):
        """WATER CANNON: an elemental fire move. Massive dmg to Fire type, 
        normal dmg to Water type, minimal dmg to Grass type. """

    print(f"Pykemon {self.name} used {self.moves[3]}!")

    # Generate damage based on enemy type:
    if enemy.element == "fire":
        print("It's SUPER effective!")
        damage = random.randint(35, 50)
    elif enemy.element == "grass":
        print("It's not very effective...")
        damage = random.randint(5, 10)
    else:
        damage = random.randint(10, 30)

    # Deal damage
    print(f"It dealt {damage} damage,")
    enemy.current_health -= damage

    
    def move_info(self):
        """ Display pykemon move info """
        print(f"\n{self.name} Moves:")
        
        # Light
        print(f"-- {self.moves[0]} --")
        print("\tAn efficient attack...\n\tGuaranteed to do damage within the range of 15 to 25 damage points.\n")
        # Heavy attack
        print(f"-- {self.moves[1]} --")
        print("\tA risky attack...\n\tCould deal up to 50 damage points or as little as 0 damage points\n")
        # Restorative move
        print(f"-- {self.moves[2]} --")
        print("\tA restorative move...\n\tGuaranteed to heal your Pykemon 15 to 25 health points\n")
        # Elemental attack
        print(f"-- {self.moves[3]} --")
        print("\tA powerful WATER based attack...\n\tGuaranteed to deal MASSIVE damage to FIRE type Pykemon\n")



class Grass(Pykemon):
    """ A Grass based Pykemon that is a child of the Pykemon class. """

    def __init__(self, name, element, health, speed):
        """ Initialise attributes from the parent Pykemon class."""
        super().__init__(self, name, element, health, speed)
        # Move list unique to all Grass type Pykemon
        moves = ["Vine Whip", "Wrap", "Grow", "Leaf Blade"]


    def special_attack(self, enemy):
        """LEAF BLADE: an elemental grass move. Massive dmg to Water type, 
        normal dmg to Grass type, minimal dmg to Fire type. """

    print(f"Pykemon {self.name} used {self.moves[3]}!")

    # Generate damage based on enemy type:
    if enemy.element == "water":
        print("It's SUPER effective!")
        damage = random.randint(35, 50)
    elif enemy.element == "fire":
        print("It's not very effective...")
        damage = random.randint(5, 10)
    else:
        damage = random.randint(10, 30)

    # Deal damage
    print(f"It dealt {damage} damage,")
    enemy.current_health -= damage

    
    def move_info(self):
        """ Display pykemon move info """
        print(f"\n{self.name} Moves:")
        
        # Light
        print(f"-- {self.moves[0]} --")
        print("\tAn efficient attack...\n\tGuaranteed to do damage within the range of 15 to 25 damage points.\n")
        # Heavy attack
        print(f"-- {self.moves[1]} --")
        print("\tA risky attack...\n\tCould deal up to 50 damage points or as little as 0 damage points\n")
        # Restorative move
        print(f"-- {self.moves[2]} --")
        print("\tA restorative move...\n\tGuaranteed to heal your Pykemon 15 to 25 health points\n")
        # Elemental attack
        print(f"-- {self.moves[3]} --")
        print("\tA powerful GRASS based attack...\n\tGuaranteed to deal MASSIVE damage to WATER type Pykemon\n")



# Game class
class Game():
    """ A game object to control the creation and flow of pykemon and simulate battle! """

    def __init__():



    def create_pykemon():



    def choose_pykemon():



    def get_attack():



    def player_attack():



    def computer_attack():



    def battle():


print("""
Welcome to Pykemon!

Can you become the world's greatest Pykemon Trainer???

Don't worry! Prof 5ubt13 is here to help you on your quest.
He would like to gift you your first Pykemon!

Here are three potential Pykemon partners:
""")

input("Press (enter) to choose your Pykemon!")

























