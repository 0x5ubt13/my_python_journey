# Inheritance

# Parent class -----> Child class

# The Parent Class
class Dog():
    """ Class to represent a general dog """

    def __init__(self, name, gender, age, loud):
        """ Initialize attributes """
        self.name = name.title()
        self.gender = gender
        self.age = age
        self.is_loud = loud # loud is a bool

    def call_dog(self):
        """ Call the dog """
        if self.gender == "male":
            print(f"Here {self.name}! Good boy!")
        else:
            print(f"Here {self.name}! Good girl!")

    def dog_years(self):
        """ Compute age in dog years """
        dog_years = self.age * 7
        print(f"{self.name} is {dog_years} years old in dog years.")

    def bark(self):
        """ Get the dog to speak """
        if self.is_loud:
            print("WOOF WOOF WOOF!!!!")
        else: 
            print("woof")

# A child class: Beagle
class Beagle(Dog):
    """ A class to represent a specific type of dog """

    def __init__(self, name, gender, age, loud, gunshy):
        """ Initialize attributes from the parent class. """
        super().__init__(name, gender,age,loud)
        self.is_gunshy = gunshy # A bool

    def bark(self):
        """ Get the dog to speak """
        if self.is_loud:
            print("HOOOOOOOWWWWWLLLLLLL!!!!")
        else: 
            print("howl")

    def go_hunt(self):
        """ If the dog is not gunshy, take them hunting """
        if not self.is_gunshy:
            self.bark()
            print(f"{self.name} just brought back a duck.")
        else:
            print(f"{self.name} is not a good hunting dog.")

class Chihuahua(Dog):
    """ Represents a specific type of dog. """
    
    def __init__(self, name, gender, age, loud):
        """ Initialize attributes from the parent class. """
        super().__init__(name, gender, age, loud)

    def bark(self):
        if self.is_loud:
            print('YIP YIP YIP YIP YIP YIP YIP YIP YIP!!!')
        else:
            print("yip")


my_dog = Dog('spot', 'male', 3, True)
print(my_dog.name)
print(my_dog.age)

my_dog.call_dog()
my_dog.dog_years()
my_dog.bark()

your_dog = Beagle("lassie", "female", 8, False, False)

print(my_dog)
print(your_dog)
print(type(my_dog))
print(type(your_dog))

your_dog.call_dog()
your_dog.dog_years()
your_dog.bark()

your_dog.go_hunt()

tiny_dog = Chihuahua("tiny", "male", 2, True)
tiny_dog.call_dog()
tiny_dog.dog_years()
tiny_dog.bark()
