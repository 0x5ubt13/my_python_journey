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
        print(f"Pykemon {self.name} used {self.moves[2]}")
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
        super().__init__(name, element, health, speed)
        # Move list unique to all Fire type Pykemon
        self.moves = ["Scratch", "Ember", "Light", "Fire Blast"]


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
        # Restore move
        print(f"-- {self.moves[2]} --")
        print("\tA restorative move...\n\tGuaranteed to heal your Pykemon 15 to 25 health points\n")
        # Elemental attack
        print(f"-- {self.moves[3]} --")
        print("\tA powerful FIRE based attack...\n\tGuaranteed to deal MASSIVE damage to GRASS type Pykemon\n")



class Water(Pykemon):
    """ A Water based Pykemon that is a child of the Pykemon class. """

    def __init__(self, name, element, health, speed):
        """ Initialise attributes from the parent Pykemon class."""
        super().__init__(name, element, health, speed)
        # Move list unique to all Water type Pykemon
        self.moves = ["Bite", "Splash", "Dive", "Water Cannon"]


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
        super().__init__(name, element, health, speed)
        # Move list unique to all Grass type Pykemon
        self.moves = ["Vine Whip", "Wrap", "Grow", "Leaf Blade"]


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
        # Restore move
        print(f"-- {self.moves[2]} --")
        print("\tA restorative move...\n\tGuaranteed to heal your Pykemon 15 to 25 health points\n")
        # Elemental attack
        print(f"-- {self.moves[3]} --")
        print("\tA powerful GRASS based attack...\n\tGuaranteed to deal MASSIVE damage to WATER type Pykemon\n")



# Game class
class Game():
    """ A game object to control the creation and flow of pykemon and simulate battle! """

    def __init__(self):
        """ Initialize attributes """
        # Upon creating a pykemon, element and name would be chosen randomly
        self.pykemon_elements = ["fire", "water", "grass"]
        self.pykemon_names = ["Chewdie", "Spatol", "Burnmander", "Pykachu", "Pyonx", "Abbacab", "Sweetil", 
                              "Jampot", "Swagilybo", "Muttle", "Zantbat", "Wiggly Poof", "Rubblesaur"]
        self.battles_won = 0


    def create_pykemon(self):
        """ Randomly generate a pykemon!"""
        # Randomly generate health and speed attributes
        health = random.randint(70, 100)
        speed = random.randint(1, 10)

        # Randomly choose an element and name
        element = self.pykemon_elements[random.randint(0, len(self.pykemon_elements)-1)]
        name = self.pykemon_names[random.randint(0, len(self.pykemon_names)-1)]

        # Create the right element pykemon
        if element == "fire":
            pykemon = Fire(name, element, health, speed)
        elif element == "water":
            pykemon = Water(name, element, health, speed)
        elif element == "grass":
            pykemon = Grass(name, element, health, speed)

        return pykemon


    def choose_pykemon(self):
        """ A method to simulate choosing a starting Pykemon similar to Pokemon """
        # A list to hold 3 starter pykemon
        starters = []

        # Pick 3 different elemental type pykemon for the starter list
        while len(starters) < 3:
            # Make a starter pykemon
            pykemon = self.create_pykemon()

            # Bool to determine whether or not it's unique and shoild be added to the starters list
            valid_pykemon = True
            for starter in starters:
                # Check if the name or element is already used by another starter
                if starter.name == pykemon.name or starter.element == pykemon.element:
                    valid_pykemon = False
            # The created pykemon is unique, add it to the list starter
            if valid_pykemon:
                starters.append(pykemon)

        # Starters list is complete, show off the starter pykemon:
        for starter in starters:
            starter.show_stats()
            starter.move_info()

        # Present information to user
        print("\nProfessor 5ubt13 presents you with three Pykemon:")
        print("(1) - " + starters[0].name)
        print("(2) - " + starters[1].name)
        print("(3) - " + starters[2].name)
        choice = int(input("Which Pykemon would you like to choose: "))
        pykemon = starters[choice-1]

        return pykemon

    def get_attack(self, pykemon):
        """ Get a users attack choice """
        # Show the moves list using pykemon specific move names
        print("\nWhat would you like to do...")
        print(f"(1) - {pykemon.moves[0]}")
        print(f"(2) - {pykemon.moves[1]}")
        print(f"(3) - {pykemon.moves[2]}")
        print(f"(4) - {pykemon.moves[3]}")
        choice = int(input("Please enter your move choice: "))
        
        # Formatting
        print("\n-------------------------------------------------")

        return choice


    def player_attack(self, move, player, computer):
        """ Attack the computer AI """
        # Call the appropriate attack method based on the given move
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)

        # Check if the computer has fainted
        computer.faint()

    def computer_attack(self, player, computer):
        """ Let the computer AI attack the player """
        # Randomly pick a move for the computer to execute
        move = random.randint(1, 4)

        # Call the appropriate method based on the given move
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)

        # Check to see if the player has fainted
        player.faint()
        

    def battle(self, player, computer):
        # Get the player move for the round
        move = self.get_attack(player)

        # If the player is faster they go first
        if player.speed >= computer.speed:            
            # Player attacks
            self.player_attack(move,player,computer)
            if computer.is_alive:
                #Computer is still alive, let them attack
                self.computer_attack(player, computer)
        # The player's pykemon is slower than the computer: the computer goes first
        else:
            self.computer_attack(player, computer)

            # Player is still alive, let them attack
            if player.is_alive:
                self.player_attack(move, player, computer)


# Main code
print("""
Welcome to Pykemon!

Can you become the world's greatest Pykemon Trainer???

Don't worry! Prof 5ubt13 is here to help you on your quest.
He would like to gift you your first Pykemon!

Here are three potential Pykemon partners:
""")

input("Press (enter) to choose your Pykemon!")

# The main game loop
playing_main = True
while playing_main:
    # Create a game instance
    game = Game()

    # Choose your starter pykemon
    player = game.choose_pykemon()
    print(f"\nCongratulations Trainer, you have chosen {player.name}!")
    input(f"\nYour Journey with {player.name} begins now... Press enter!")

    # While your pykemon is alive, continue to do battle
    while player.is_alive:
        # Create a computer pykemon to battle
        computer = game.create_pykemon()
        print(f"\nOh no! A wild {computer.name} has approached!")
        computer.show_stats()
        
        # While both pykemon are alive, engage in combat
        while computer.is_alive and player.is_alive:
            game.battle(player, computer)
            
            # Both parties survived the round, show their current stats
            if computer.is_alive and player.is_alive:
                player.show_stats()
                computer.show_stats()
                # Formatting
                print("\n-------------------------------------------------")

        # If the player survived the battle, increment battles won
        if player.is_alive:
            game.battles_won += 1

    # The player has finally fainted
    print(f"\nPoor {player.name} has fainted")
    print(f"But not before defeating {game.battles_won} Pykemon!")
    # Ask the user if they want to play again
    choice = input("Would you like to play again? (y/n): ")
    if choice != 'y':
        playing_main = False
        print("Thank you for playing Pykemon!")
        
            






# To-do:

# - Adding more classes
# - Reviewing and improving the code


















