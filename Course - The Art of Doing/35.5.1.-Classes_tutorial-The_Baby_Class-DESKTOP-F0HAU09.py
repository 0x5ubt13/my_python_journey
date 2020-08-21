# Creating a Class

# Class --> Blueprint to build something
# Object --> What you build
# Instance --> What you work with once it is built
# Attribute --> Info used to distinguish one instance from another in a class
# Method --> Behaviour common to all instances of a class (functions)
from random import randint

class Baby():
    """ A simple class to simulate a baby """

    def __init__(self, name, gender, age): 
        """ Initialize attributes """
        self.name = name.title()
        self.gender = gender
        self.age = age

        self.tired = True

    def play(self):
        """ Simulate playing based on gender """
        if self.gender == "male":
            print(self.name + " is playing with cars.")
        else:
            print(self.name + " is playing with blocks.")

    def cry(self):
        """ Simulate crying """
        print("WAAAH WAAH WAAAAAHHH!!!!")
        print("Even " + str(self.age) + " year olds cry.")

    def sleep(self):
        if self.tired:
            print(self.name + " is sleeping... FINALLY!!")
            self.tired = False
        else:
            print("Sorry! " + self.name + " isn't tired.")
    
wee_boy = Baby("leo", "male", 4)
wee_girl = Baby("sophia", "female", 3)

print(wee_boy.name)
print(wee_girl.name)

print(wee_boy.gender)
print(wee_girl.age)

print(wee_boy.tired)

print(wee_boy.name + " is a " + str(wee_boy.age) + " year old " + wee_boy.gender + ".")
print(wee_girl.name + " is a " + str(wee_girl.age) + " year old " + wee_girl.gender + ".")

wee_boy.play()
wee_girl.play()

wee_boy.cry()
wee_girl.cry()

wee_boy.sleep()
wee_girl.sleep()

wee_boy.sleep()
wee_girl.sleep()

babies = []
for i in range(100):
    num = randint(0, 1)
    if num == 0:
        gender = "male"
    else:
        gender = 'female'

    age = randint(0, 5)

    baby = Baby(str(i), gender, age)
    babies.append(baby)

for baby in babies:
    print("Baby #" + baby.name + " is a " + str(baby.age) + " year old " + baby.gender + ".")