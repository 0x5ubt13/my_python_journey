#!/usr/bin python3
from random import randint

# Thesaurus
thesaurus = {
    "hot":["balmy", "summery", "tropical", "boiling", "scorching"],
    "cold":["chilly", "cool", "freezing", "frigid", "polar"],
    "happy":["content", "cherry", "merry", "jovial", "jocular"],
    "sad":["unhappy", "downcast", "miserable", "glum", "melancholy"],
}

print('Welcome to the Thesaurus App!\n\nChoose a word from the thesaurus and I will give you a synonym.\n\nHere are the words in the thesaurus:\n\t\t- Hot\n\t\t- Cold\n\t\t- Happy\n\t\t- Sad')

while True:
    choice = input("\nWhat word would you like a synonym for: ").lower().split()
    random = randint(0, 4)
    for key, values in thesaurus.items():
        if "hot" in choice:
            if "hot" in key: 
                print("A synonym for hot is " + str(values[random]) + ".\n")
                break
        elif "cold" in choice:
            if "cold" in key:    
                print("A synonym for cold is " + str(values[random]) + ".\n")
                break
        elif "happy" in choice:
            if "happy" in key:
                print("A synonym for happy is " + str(values[random]) + ".\n")
                break
        elif "sad" in choice:
            if "sad" in key:
                print("A synonym for hot is " + str(values[random]) + ".\n")
                break
    
    reveal = input("Do you want to see the whole thesaurus? (yes/no): ")
    while True:
        if reveal.startswith("y"):
            for key, values in thesaurus.items():
                print("\n" + key.title() + "'s synonyms are:")
                for value in values:
                    print("\t- " + value.title())
        elif reveal.startswith("n"):
            print("I hope you enjoyed the program. Thank you!")
        else:
            print("Not a valid answer. Please answer yes or no.")
            continue
        break
    break
#would you like to see the whole thesaurus: