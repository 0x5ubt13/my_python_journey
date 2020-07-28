#!/usr/bin python3

characters_allowed = "qwertyuiopasdfghjklzxcvbnm"
characters_parsed = []
count_characters_parsed = 0
count_phrase_1 = {}
phrase_1_sorted_letters = []

phrase_1 = input("Welcome to the Frequency Analysis App.\n\nEnter a word or phrase to count the occurrence of each letter: ").lower().replace(" ","")

for char in phrase_1:
    if char in characters_allowed:
        characters_parsed.append(char)
        count_characters_parsed += 1

print(characters_parsed)
characters_parsed.sort()
print(characters_parsed)

for char in characters_parsed:    
    if char in count_phrase_1:
        count_phrase_1[char] += 1
    else:
        count_phrase_1[char] = 1

print("Here is the frequency analysis from key phrase #1 sorted alphabetically:\n\n\tLetter\t\tOccurrence\t\tPercentage")
for k, v in count_phrase_1.items():
    print("\t" + k + "\t\t" + str(v) + "\t\t" + str(round((v * 100 / count_characters_parsed), 2)) + "%")

print("Letters ordered from highest occurrence to lowest:")
sorted_by_freq_phrase_1 = sorted(count_phrase_1.items(), key = lambda t: t[1], reverse = True)
for pair in sorted_by_freq_phrase_1:
    phrase_1_sorted_letters.append(pair[0])
print("".join(phrase_1_sorted_letters))