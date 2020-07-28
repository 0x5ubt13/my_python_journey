#!/usr/bin/env python3
import math

print('Welcome to 5ubt13\'s Right Triangle solver program!!')

first_leg = float(input('What is the value of the first leg of the triangle: '))
second_leg = float(input('What is the value of the second leg of the triangle: '))

hypotenuse = round(math.sqrt(first_leg ** 2 + second_leg ** 2), 3) 
area = round(first_leg * second_leg / 2, 3)

print(f'For a triangle with legs of {first_leg} and {second_leg}:\n The hypotenuse is: {hypotenuse} \n The area is: {area}')
