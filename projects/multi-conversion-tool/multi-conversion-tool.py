#!/usr/bin/env python3
import base64
import codecs

# --------------------------- Declaring classes --------------------------- #

class Decoder():
    """ A class to rule all them encodings """

    def __init__(self):
        """ Initialise attributes """
        self.flag = ""



    def base_64(self, encoded_msg):
        """ Decode a base64 string to plaintext """

        # Loop to help avoiding padding error. Modulo operation makes sure the padding is correct
        while len(encoded_msg) %4 != 0: 
            encoded_msg += '='
        
        # Once we have the correct padding, decode it to the flag var
        self.flag = base64.b64decode(encoded_msg).decode('utf-8')
        
        return self.flag




class Decrypter():
    """ A class to rule all them encryptions """

    def __init__(self):
        """ Initialise attributes """
        self.flag = ""
    


    def rot_13(self, encrypted_msg):
        """ Decrypt a rot 13 encoded msg using codecs module """

        self.flag = codecs.decode(encrypted_msg, 'rot-13')
        
        return self.flag

    """
    future project rot 47:
    def rot_47(self, encrypted_msg):
        "" Decode a rot 47 encoded msg ""

        return self.flag
    """




class Deobfuscator():

    def __init__(self):
        self.flag = ""


    def ascii_ords(self, obfuscated_msg):
        """ Decode an ascii reference numbers encoded msg """

        # Declaring needed local vars
        x = 0
        code = []
        numbers = []
        output = []
        final_output = []

        # for loop to get the numbers appended in the numbers list
        for _ in obfuscated_msg:
            if obfuscated_msg[x].isnumeric() == True:
                numbers.append(int(code[x]))   
            x += 1

        # for loop to decode the ascii values
        for i in numbers:
            i = chr(i)
            output.append(i)
        
        # resetting vars
        x = 0
        y = 0

        # statement to check all the decoded chars match the obfuscated chars
        if len(output) == len(obfuscated_msg):
            final_output = output[:] # We use a slice to avoid using twice the same list

        else:
            # Putting everything together in order, 1 character at a time
            for i in code:
                if code[x].isnumeric() == True:
                    final_output.append(output[y])
                    y += 1
                else:
                    final_output.append(code[x])
                x += 1
        self.flag = ''.join(final_output)

        return self.flag



    def hex2ascii(self, obfuscated_msg):
        """ Get those hex bytes transformed to plaintext """

        self.flag = bytes.fromhex(obfuscated_msg).decode('UTF-8')

        return self.flag




class Main():
    """ Main program flow control """

    def __init__(self):
        self.first_selection = 0
        self.second_selection = 0
        self.on = True



    def greeting_msg(self):
        """ Print greeting msg and get first selection from user """

        print('''
        Welcome to 0x5ubt13\'s string multi-converter.
        Please choose one of the following options:

        +------------------+
        |                  |
        |    1. Decode     |
        |                  |
        |    2. Decrypt    |
        |                  |    
        |  3. Deobfuscate  |
        |                  |
        +------------------+
        
        ''')

        self.first_selection = int(input('Your selection ("1" / "2"): ').strip())
        
        return self.first_selection


    
    def second_selection_msg(self, first_selection):
        """ Take first_selection input, then get second_selection """ 

        if self.first_selection == 1:
            print('''
            Please select in which type of encoding your string seems to be:

            +----------------+
            |                |
            |   1. Base 64   |
            |                |
            |  2. Stay tuned |
            |                |
            +----------------+
            
            ''')
            
            self.second_selection = int(input('Your selection ("1" / "2"): ').strip())

            if self.second_selection == 1:
                self.second_selection = "b64"
            else:
                self.second_selection = ""


        elif self.first_selection == 2:
            print('''
            Please select in which type of encryption your string seems to be:

            +-----------------+
            |                 |
            |    1. Rot 13    |
            |                 |
            |  2. Stay tuned  |
            |                 |
            +-----------------+
            
            ''')
            
            self.second_selection = int(input('Your selection ("1" / "2"): ').strip())

            if self.second_selection == 1:
                self.second_selection = "rot13"
            else:
                self.second_selection = ""


        elif self.first_selection == 3:
            print('''
            Please select in which type of obfuscation your string seems to be:

            +-----------------+
            |                 |
            |    1. Ascii     |
            |                 |
            |  2. Hexadecimal |
            |                 |
            +-----------------+
            
            ''')
            
            self.second_selection = input('Your selection ("1" / "2"): ')
            

            if self.second_selection == '1':
                self.second_selection = "ascii"
            elif self.second_selection == '2':
                self.second_selection = "hex"

        # Returning the selection
        return self.second_selection



    def program_killer(self):
        """ Ending the while loop """

        again = input("Do you want to process a different string?\nEnter yes to confirm or any other key to exit: ")
        if again.startswith('y') and again == 'y' or again == 'yes':
            print("Restarting the program...")
        else:
            self.on = False




# --------------------------- Initialising program --------------------------- #

decoder = Decoder()
decrypter = Decrypter()
deobfuscator = Deobfuscator()
main = Main()

while main.on == True:
    # Selecting the correct converter
    first_choice = main.greeting_msg()
    second_choice = main.second_selection_msg(first_choice)

    # Control flow
    if second_choice == 'b64':
        encoded_msg = input("Please paste here your encoded string: ").strip()
        flag = decoder.base_64(encoded_msg)
        print(flag)

    if second_choice == 'rot13':
        encrypted_msg = input("Please paste here your encrypted string: ").strip()
        flag = decrypter.rot_13(encrypted_msg)
        print(flag)

    if second_choice == 'ascii':
        obfuscated_msg = input("Please paste here your encoded string: ").split()
        flag = deobfuscator.ascii_ords(obfuscated_msg)
        print(flag)

    if second_choice == 'hex':
        encoded_msg = input("Please paste here your encoded string: ").strip().lower
        flag = deobfuscator.hex2ascii(encoded_msg)
        print(flag)

    main.program_killer()

print('Thanks for using my app! Have a nice day!')
