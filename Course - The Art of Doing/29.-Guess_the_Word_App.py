#!/usr/bin/python3
from random import randint

# Initializing program
categories = {
    "Sports":["Football", "Baseball", 'Rugby', 'Basketball', 'Volleyball', 'Athletism', 'Soccer'],
    "Fruits":['Strawberry', 'Apple', 'Orange', 'Peach', 'Watermelon', 'Banana', 'Plum'],
    "Music bands":['Iron Maiden', 'The Who', 'Foo Fighters', 'Nirvana', 'The Strokes', 'Daft Punk', 'Metallica'],    
    "Brands":['Apple', 'Motorola', 'Google', 'Asus', 'Acer', 'Samsung', 'Toshiba'],
}

# Counter
x = 0 

# Randomising the key
def rand_cat():
    global randcat
    rand = randint(0, 3)
    randcat = list(categories.keys())[rand] # In order to index the key in python3, we need to parse .keys() to a list since the method returns an iterable but not indexable object!!!
    return

# Randomising the value
def rand_val():
    global word
    global counter
    word = []
    rand = randint(0, 6)
    key = randcat
    randval = categories[key][rand]
    counter = 0
    # Getting the number of letters of the word to guess
    for letter in randval:
        if letter.isalpha():
            counter += 1
        word.append(letter)
        #printable_word = "".join(word)
    return

# Defining the input function
def guess():
    global guess
    global x
    
def hide_word():
    global hidden_word
    hidden_word = []
    for letter in word:
        if letter.isalpha():
            hidden_word.append("-")
        else:
            hidden_word.append(letter)
    #printable_hidden_word = "".join(hidden_word)
    return 

# Starting the program
print("Welcome to Guess the Word App!")
while True:
    rand_cat()
    rand_val()
    hide_word()

    print(f"Guess a {counter} letters word from the following category: {randcat}")
    print("".join(hidden_word))

    while guess != word:
        guess = input("Make your guess! ").title()
        x += 1
        if guess == "".join(word).title():
            print("Well done!!!")
            break
        elif hidden_word == word:
            print("Oh no!! You've run out of opportunities!")
            break
        else:
            print("That is not correct. Let us reveal a letter to help you!\n")
            while True:
                index = randint(0, len(word) - 1)
                #print(index) Added for debugging purposes
                if hidden_word[index] == "-":
                    hidden_word[index] = word[index]
                    print("".join(hidden_word))
                    break
                else:
                    if "-" not in hidden_word:
                        break
                    continue

    print("The word was " + "".join(word) + "\n")
    if guess == "".join(word).title():
        print("You guessed it in " + str(x) + " guesses.")
    yorn = input("Would you like to play again? (y/n) ").lower().strip()
    if yorn == 'y' or yorn == 'yes':
        continue
    else:
        break







