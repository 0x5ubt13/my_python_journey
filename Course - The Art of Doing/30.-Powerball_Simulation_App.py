#!/usr/bin/python3

chance = 1
chance_red_balls = 1

# Greeting and getting input from user
print("-"*10 + " Power-Ball Simulator " + "-"*10)
white_balls = int(input("How many white-balls to draw from for the 5 winning numbers (normally 69)? "))
red_balls = int(input("How many red-balls to draw from for the Power-Ball (normally 26)? "))
for n in range(6, 1, -1):
    chance *= white_balls
    white_balls -= 1
    print(white_balls)
    print(chance)
chance /= red_balls
print(chance)
#print(f"You have a 1 in {chance} chance of winning this lottery.")
#interval = int(input("Purchase tickets in what interval? "))



