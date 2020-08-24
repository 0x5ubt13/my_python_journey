#!/usr/bin/python3
import random
import time

class Game():
    """ Coding the game behaviour """

    def __init__(self, money=100):
        """ Initialising the Class """
        
        self.money = money
        
        self.bet = 0
        # List to get the cards off the pool once drew
        self.used_cards = []
        # We need to define all 53 cards used in Blackjack
        self.deck = {
            "Hearts":["Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "J of Hearts", "Q of Hearts", "K of Hearts"], 
            "Spades":["Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "J of Spades", "Q of Spades", "K of Spades"],
            "Diamonds":["Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "J of Diamonds", "Q of Diamonds", "K of Diamonds"], 
            "Clubs":["Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "J of Clubs", "Q of Clubs", "K of Clubs"], 
        }
        self.values = 0
        self.players_hand = []
        self.players_score = 0
        self.houses_hand = []
        self.houses_score = 0
        self.turn = 0

    
    def draw(self):
        """ We need a method for randomly drawing a card, erase it from the pool and assigning it a value """
        
        while True:
            # Randomising keys and values from the Deck dictionary    
            randomising_suit = random.randint(0, 3)
            randomising_card = random.randint(0, 12)

            # In order to index the key in python3, we need to parse .keys() to a list since the method returns an iterable but not indexable object!!!
            randsuit = list(self.deck.keys())[randomising_suit] 
            randcard = self.deck[randsuit][randomising_card]
            
            # Checking if the card is already been drawn
            if randcard in self.used_cards:
                continue

            # Assigning initial values to the cards
            if randcard.startswith("A"):
                self.values += 11
            elif randcard.startswith("2"):
                self.values += 2
            elif randcard.startswith("3"):
                self.values += 3
            elif randcard.startswith("4"):
                self.values += 4
            elif randcard.startswith("5"):
                self.values += 5
            elif randcard.startswith("6"):
                self.values += 6
            elif randcard.startswith("7"):
                self.values += 7
            elif randcard.startswith("8"):
                self.values += 8
            elif randcard.startswith("9"):
                self.values += 9
            elif randcard.startswith("10") or randcard.startswith("J") or randcard.startswith("Q") or randcard.startswith("K"):
                self.values += 10

            # Appending it to the list of used cards below takes them off of the drawing pool
            self.used_cards.append(randcard)
            break
        return(randcard)
    
    def betting(self):
        """ Method to set the bet and show the first card of the dealer """
        
        print(f"Current money: £{self.money}")
        while True:
            self.bet = int(input("What would you like to bet (minimum bet of £20): "))

            # Since the minimum bet is £20, we need a little control flow to meet this criteria
            if self.bet < 20:
                self.bet = 20
            
            
            if self.bet > self.money:
                print("You don't have money enough to make that bet.") 
                continue

            break
        self.money -= self.bet

        # Printing a summary for the player and showing the first dealer's card    
        print(f"Current money: £{self.money}  |  Current bet: £{self.bet}")
        print(f"\nThe dealer is showing a {self.houses_hand[0]}\n")



    def house_turn(self):
        """ Method to make the house play """

        self.turn += 1
        if self.turn == 1:
            self.houses_hand.append(self.draw())
            self.houses_score += self.values
            self.values = 0
        elif self.turn == 2:
            self.houses_hand.append(self.draw())
            self.houses_score += self.values
            self.values = 0
            while self.houses_score <= 16:                
                self.houses_hand.append(self.draw())
                self.houses_score += self.values
                self.values = 0


    def player_turn(self):
        """ Method to make the player play """

        print("Your cards:")
        for i in range(2):
            self.players_hand.append(self.draw()) 
            self.players_score += self.values
            self.values = 0
        for card in self.players_hand:
            print(card)
        print("Total value: ", self.players_score)
        
        while True:
            hit = input("Do you want to hit? (y/n) ").lower().strip()
            if hit == "y":
                print("hit y")
                self.players_hand.append(self.draw()) 
                self.players_score += self.values
                self.values = 0
                for card in self.players_hand:
                    print(card)
                print("Total value: ", self.players_score)
    
                if self.players_score >= 22:
                    break
            else:
                break
        if len(self.players_hand) == 2 and "A" in self.players_hand and self.players_score == 21:
            print("Congratulations, you've scored a Blackjack!!!!")


    def reveal_houses_hand(self):
        """ Reveal the dealer's hand and and finishes the game """
        
        print("\nDealer is set with a total of", len(self.houses_hand), "cards.")
        input("\nPress (enter) to reveal the dealer's hand.")
        for card in self.houses_hand:
            time.sleep(0.5)
            print(card)
        if self.players_score >= 22:
            print("You went over 21... You loose!")
        else:
            if self.players_score == self.houses_score:
                print(f"Dealer gets {self.houses_score}.")
                print("It's a tie!!")
                self.money += self.bet
            else:
                if self.houses_score >= 22:
                    print("Dealer went over 21... You win!")
                    self.money += self.bet * 2
                else:
                    if len(self.players_hand) == 2 and "A" in self.players_hand and self.players_score == 21:
                        print("You've scored a Blackjack!!!!")
                        self.money += self.bet * 3
                    else:
                        if self.players_score > self.houses_score:
                            print(f"Dealer gets {self.houses_score}.")
                            print("You win!!")
                            self.money += self.bet * 2
                        else:
                            print(f"Dealer gets {self.houses_score}.")
                            print("The House wins!")

    def wipe(self):
        """ Wipes the game out when a round is finished """

        # Re-declaring variables
        self.values = 0
        self.players_hand = []
        self.players_score = 0
        self.houses_hand = []
        self.houses_score = 0
        self.turn = 0

        # Checking the deck
        if len(self.used_cards) > 45:
            print("There are only", 52 - len(self.used_cards), "cards to play with. Shuffling...")
            self.used_cards = []


 
print("Welcome to the Blackjack App.")
print("The minimum bet at this table is £20.")
game = Game(int(input("How much money are you willing to play with today? £")))

while game.money > 0:
    game.house_turn()
    game.betting()
    game.player_turn()
    game.house_turn()
    game.reveal_houses_hand()
    game.wipe()

print("\nSorry, you ran out of money. Please play again.")


""" 
To do:
- Merging 2nd house_turn() into reveal_houses_hand()
- Reviewing reveal_houses_card() control flow to erase indentation
- Creating artwork for cards
- Reviewing comments
- Adding functionality to make the Ace's value both 1 and 11

"""