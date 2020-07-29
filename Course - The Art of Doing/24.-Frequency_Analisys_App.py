#!/usr/bin python3

# Initializing vars
characters_allowed = "qwertyuiopasdfghjklzxcvbnm"
characters_parsed = []
characters_parsed_2 = []
count_characters_parsed = 0
count_characters_parsed_2 = 0
count_key_phrase_1 = {}
count_key_phrase_2 = {}
key_phrase_1_sorted_letters = []
key_phrase_2_sorted_letters = []

# Starting the program
key_phrase_1 = input("Welcome to the Frequency Analysis App.\n\nEnter a word or phrase to count the occurrence of each letter: ").lower().replace(" ","")

# For loop for parsing the input to only letters and sorting them alphabetically afterwards
for char in key_phrase_1:
    if char in characters_allowed:
        characters_parsed.append(char)
        count_characters_parsed += 1
characters_parsed.sort()
# print(characters_parsed) # Adding this line for debugging purposes

# For loop for counting the total number of letters, adding them to a new dictionary
for char in characters_parsed:    
    if char in count_key_phrase_1:
        count_key_phrase_1[char] += 1
    else:
        count_key_phrase_1[char] = 1

# Printing out to the user the first analysis
print("Here is the frequency analysis from key phrase #1 sorted alphabetically:\n\n\tLetter\t\tOccurrence\t\tPercentage")
for k, v in count_key_phrase_1.items():
    print("\t" + k + "\t\t" + str(v) + "\t\t" + str(round((v * 100 / len(characters_parsed)), 2)) + "%")

# Printing out a single string with the most used letters
print("Letters ordered from highest occurrence to lowest:")
sorted_by_freq_key_phrase_1 = sorted(count_key_phrase_1.items(), key = lambda t: t[1], reverse = True)
for pair in sorted_by_freq_key_phrase_1:
    key_phrase_1_sorted_letters.append(pair[0])
print("".join(key_phrase_1_sorted_letters))

# Starting a second analysis
key_phrase_2 = input("\nEnter a new word or phrase to count the occurrence of each letter again: ").lower().replace(" ","")

# For loop for parsing the input to only letters and sorting them alphabetically afterwards
for char in key_phrase_2:
    if char in characters_allowed:
        characters_parsed_2.append(char)
        count_characters_parsed_2 += 1
characters_parsed_2.sort()

# For loop for counting the total number of letters, adding them to a new dictionary
for char in characters_parsed_2:    
    if char in count_key_phrase_2:
        count_key_phrase_2[char] += 1
    else:
        count_key_phrase_2[char] = 1

# Printing out to the user the second analysis
print("Here is the frequency analysis from key phrase #2 sorted alphabetically:\n\n\tLetter\t\tOccurrence\t\tPercentage")
for k, v in count_key_phrase_2.items():
    print("\t" + k + "\t\t" + str(v) + "\t\t" + str(round((v * 100 / len(characters_parsed_2)), 2)) + "%")

# Printing out a single string with the most used letters
print("Letters ordered from highest occurrence to lowest:")
sorted_by_freq_key_phrase_2 = sorted(count_key_phrase_2.items(), key = lambda t: t[1], reverse = True)
for pair in sorted_by_freq_key_phrase_2:
    key_phrase_2_sorted_letters.append(pair[0])
print("".join(key_phrase_2_sorted_letters))