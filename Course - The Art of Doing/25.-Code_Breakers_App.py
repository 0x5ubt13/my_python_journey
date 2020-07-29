#!/usr/bin python3

# This exercise is a continuation from exercise 24 and therefore the code will be overall a copy of it

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
# Uncommenting first line of ex.24 and hard coding a reference text
#phrase_1 = input("Welcome to the Frequency Analysis App.\n\nEnter a word or phrase to count the occurrence of each letter: ").lower().replace(" ","")
key_phrase_1 = """ 
To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any other name. In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind. He was, I take it, the most perfect reasoning and observing machine that the world has seen, but as a lover he would have placed himself in a false position. He never spoke of the softer passions, save with a gibe and a sneer. They were admirable things for the observer excellent for drawing the veil from men's motives and actions. But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted temperament was to introduce a distracting factor which might throw a doubt upon all his mental results. Grit in a sensitive instrument, or a crack in one of his own highpower lenses, would not be more disturbing than a strong emotion in a nature such as his. And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious and questionable memory. I had seen little of Holmes lately. My marriage had drifted us away from each other. My own complete happiness, and the homecentred interests which rise up around the man who first finds himself master of his own establishment, were sufficient to absorb all my attention, while Holmes, who loathed every form of society with his whole Bohemian soul, remained in our lodgings in Baker Street, buried among his old books, and alternating from week to week between cocaine and ambition, the drowsiness of the drug, and the fierce energy of his own keen nature. He was still, as ever, deeply attracted by the study of crime, and occupied his immense faculties and extraordinary powers of observation in following out those clues, and clearing up those mysteries which had been abandoned as hopeless by the official police. From time to time I heard some vague account of his doings: of his summons to Odessa in the case of the Trepoff murder, of his clearing up of the singular tragedy of the Atkinson brothers at Trincomalee, and finally of the mission which he had accomplished so delicately and successfully for the reigning family of Holland. Beyond these signs of his activity, however, which I merely shared with all the readers of the daily press, I knew little of my former friend and companion. 
"""

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
final_1 = "".join(key_phrase_1_sorted_letters)
print(final_1)

# Starting a second analysis
# Uncommenting second input line of ex.24 like we did with key_phrase_1 and hard coding another reference text
#phrase_2 = input("\nEnter a new word or phrase to count the occurrence of each letter again: ").lower().replace(" ","")
key_phrase_2 = """
Quite so! You have not observed. And yet you have seen. That is just my point. Now, I know that there are seventeen steps, because I have both seen and observed. By the way, since you are interested in these little problems, and since you are good enough to chronicle one or two of my trifling experiences, you may be interested in this. He threw over a sheet of thick, pink tinted notepaper which had been lying open upon the table. It came by the last post, said he. Read it aloud. The note was undated, and without either signature or address. There will call upon you tonight, at a quarter to eight o'clock, it said, "a gentleman who desires to consult you upon a matter of the very deepest moment. Your recent services to one of the royal houses of Europe have shown that you are one who may safely be trusted with matters which are of an importance which can hardly be exaggerated. This account of you we have from all quarters received. Be in your chamber then at that hour, and do not take it amiss if your visitor wear a mask. This is indeed a mystery, I remarked. What do you imagine that it means? I have no data yet. It is a capital mistake to theorise before one has data. Insensibly one begins to twist facts to suit theories, instead of theories to suit facts. But the note itself. What do you deduce from it? I carefully examined the writing, and the paper upon which it was written. The man who wrote it was presumably well to do, I remarked, endeavouring to imitate my companion's processes. Such paper could not be bought under half a crown a packet. It is peculiarly strong and stiff.
"""

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
final_2 = "".join(key_phrase_2_sorted_letters)
print(final_2)

# Declaring new vars
encoded_phrase = []
decoded_phrase = []

# Taking all the input necessary from the user
choice = input("Welcome to the Code Breakers App!\nWould you like to encode or decode? ").lower().strip()
while True:
    if choice == 'encode':
        plaintext = input("Please enter your plaintext to encode here: ").lower()
        for c, d in plaintext, final_1:
            index = plaintext.index(d)
            
            encoded_phrase.append(c)
    elif choice == 'decode':
        ciphertext = input("Please enter your ciphertext to decode here: ").lower()
        for c in ciphertext:
            decoded_phrase.append(c)
    else:
        print("Please chooose one of the following: ")
        continue
    break


