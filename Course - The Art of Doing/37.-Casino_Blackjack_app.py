#!/usr/bin/python3
import random

class Game():
    """ Coding the game behaviour """

    def __init__(self, money=100):
        self.money = money
        
        self.bet = 0
        self.used_cards = []
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

    def draw(self):
        while True:    
            randomising_suit = random.randint(0, 3)
            randomising_card = random.randint(0, 12)
            randsuit = list(self.deck.keys())[randomising_suit] # In order to index the key in python3, we need to parse .keys() to a list since the method returns an iterable but not indexable object!!!
            randcard = self.deck[randsuit][randomising_card]
            if randcard in self.used_cards:
                continue
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
            elif randcard.startswith("10") or randcard.startswith("J") or randcard.startswith("J") or randcard.startswith("K")
                self.values += 10
            
            self.used_cards.append(randcard)
            break
        return(randcard)
    
    def betting(self):
        print(f"Current money: £{self.money}")
        self.bet = int(input("What would you like to bet (minimum bet of £20): "))
        if self.bet < 20:
            self.bet = 20
        print(f"Current money: £{self.money}  |  Current bet: £{self.bet}")
        print(f"\nThe dealer is showing a {self.houses_hand[0]}")


    def house_turn(self):
        print("house's turn:")
        self.houses_hand = self.draw()
        print(self.houses_hand)



    def player_turn(self):
        print("player's turn:")
        self.players_hand = self.draw()


        
        
 
playing = True
while playing:
    print("Welcome to the Blackjack App.")
    print("The minimum bet at this table is £20.")
    game = Game(int(input("How much money are you willing to play with today? £")))

    game.house_turn()

    game.betting()



    again = input("Play again? (y/n) ").lower().strip()
    if again == "n":
        playing = False




