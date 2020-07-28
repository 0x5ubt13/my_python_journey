#!/usr/bin/env python3

how_much = 0
fahrenheit = 0
celsius = 0
kelvin = 0

print("Welcome to 5ubt13's Temperatures conversion program!")
name = input("What's your name? ").title().strip()

selection = int(input("Please select the temperature type you want to convert: \n 1.- Fahrenheit. \n 2.- Celsius. \n 3.- Kelvin. \n "))


def my_converter():
    if selection == 1:
        temperature = int(input("Please tell me how many degrees Fahrenheit you want to convert: "))
        fahrenheit = temperature
        celsius = (temperature - 32)* 5 / 9
        kelvin = celsius + 273.15
    elif selection == 2:
        temperature = int(input("Please tell me how many degrees Celsius you want to convert: "))
        fahrenheit = (temperature * 9 / 5) + 32
        celsius = temperature
        kelvin = temperature + 273.15
    elif selection == 3:
        temperature = int(input("Please tell me how many Kelvins you want to convert: "))
        kelvin = temperature        
        celsius = temperature - 273.15
        fahrenheit = (celsius * 9 / 5) + 32
    print(f'''
    Here's your table with all different temperatures, {name}!
    Temperature in Fahrenheit:     {fahrenheit}
    Temperature in Celsius:        {celsius}
    Temperature in Kelvin:         {kelvin}    
    ''')   
    

while True:
    if selection == 1 | 2 | 3:
        my_converter()
        break
    else:
        print(f"Naughty, naughty {name}. Please use 1, 2 or 3 to select your temperature units")
        selection = input("")
        continue    
