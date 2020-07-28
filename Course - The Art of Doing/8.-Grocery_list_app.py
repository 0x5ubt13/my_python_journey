#!/usr/bin/env python3
import datetime

# Create the datetime object and store the current date and time
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

foods = ['Meat', 'Cheese']

print('Welcome to the Grocery List app')
print('Current Date and Time: ' + day + '/' + month, hour + ':' + minute)

if len(foods) != 5:
    while len(foods) != 5:
        foods.append(input('Type of food to add to the grocery list: ').title())
        print('Here is your grocery list:\n', str(foods))
        print('Here is your grocery list:\n', sorted(foods), '\n')

if len(foods) > 2:
    while len(foods) > 2:
        print('Current grocery list:', len(foods), 'items.')
        scoreout = input('What food did you just buy: ').title()
        print('Removing', scoreout, 'from the list...')
        foods.remove(scoreout)
        

if len(foods) == 2:
    print('Here is your grocery list:\n', sorted(foods), '\n')
    no_food = foods.pop()
    print('Sorry, the store is out of ', no_food + '.')
    foods.insert(0, input('What food would you like instead: ').title())
    print('Here is your grocery list:\n', sorted(foods), '\n')


