#!/usr/bin/python3

class Simulation():
    """ A class to control the sumulation and help facilitate in the spread of the disease """
    
    def __init__(self):
        """ Initialize attributes """
        self.day_number = 1

        # Get simulation initial conditions from the user
        print("To simulate an epidemic outbreak, we must know the population size.")
        self.population_size = int(input("---Enter the population size: "))

        print("\nWe must first start by infecting a portion of the population.")
        self.infection_percent = float(input("---Enter the percentage (0-100) of the population to initially infect"))
        self.infection_percent /= 100

        print("\nWe must know the risk a person has to contract the disease when exposed.")
        

    


class Person():




class Population():
