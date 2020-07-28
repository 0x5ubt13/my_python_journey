#!/usr/bin/env python3
import random
heads = 0
tails = 0

# Greeting and getting times input
print("Welcome to the Coin Toss App!")
times = int(input("How many times would you like me to flip the coin? "))
choice = input("Would you like to see the result of each flip? (y/n) ").lower()

# Core of the program
print("\nFlipping!\n")
for time in range(times):
    flip = random.randint(0, 1)
    if flip == 0:
        if choice.startswith("y"):
            print("HEADS")
        heads +=1
    else:
        if choice.startswith("y"):
            print("TAILS")
        tails += 1
    if heads == tails:
        print(f"At {time + 1} flips, the number of heads and tails were equal at {heads} each")
print(f"\nResults of flipping a coin {times} times:\n\nSide\t\tCount\t\tPercentage\nHeads\t\t{heads}/{times}\t\t" + str(heads*100/times) + f"%\nTails\t\t{tails}/{times}\t\t" + str(tails*100/times) + "%")