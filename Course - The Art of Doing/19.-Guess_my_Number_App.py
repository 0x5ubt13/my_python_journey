#!usr/bin/env python3
from random import randint
number = randint(1, 20)

name = input("Hello! What is your name? ").title().strip()
print(f"Well {name}, I am thinking of a number between 1 and 20. You have 5 guesses")

for i in range(5):
    guess = int(input("Take a guess: "))
    if guess == number:
        print(f"Congratulations {name}! You have guessed my number in {i + 1} guesses!")
        break
    elif guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print(f"Game over. The number I was thinking of was {number}")

if guess != number:
    print(f"Game over. The number I was thinking of was {number}")