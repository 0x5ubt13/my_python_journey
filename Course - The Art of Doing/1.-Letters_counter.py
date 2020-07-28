#!/usr/env/python3

print('Welcome to 5ubt13\'s letters counter program!')

name = input('First of all, what\'s your name? ').title().strip()
phrase = input(f'Hello, {name}!,\n Please throw me here the phrase you want me to analise for you, I will count the number of ocurrences of the letter that you wish: \n')
letter = input('Now please tell me the letter you want me to count: ')
result = 0

phrase = phrase.lower()
letter = letter.lower()

result = phrase.count(letter)

# also doable with a for loop
#for i in phrase:
#    if i == letter:
#        result += 1
#    else: continue

print("Done! I found your letter \"" + letter + "\"", result, "times. Thanks for using me!")
