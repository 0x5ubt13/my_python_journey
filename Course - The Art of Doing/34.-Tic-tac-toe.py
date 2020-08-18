def gui():
    """getting the picture"""
    print(f'''
           Tic-Tac-Toe
        ~~~~~~~~~~~~~~~~~
        || 1 || 2 || 3 ||
        ~~~~~~~~~~~~~~~~~
        || 4 || 5 || 6 ||
        ~~~~~~~~~~~~~~~~~
        || 7 || 8 || 9 ||
        ~~~~~~~~~~~~~~~~~

           Tic-Tac-Toe
        ~~~~~~~~~~~~~~~~~
        || {numbers[0]} || {numbers[1]} || {numbers[2]} ||
        ~~~~~~~~~~~~~~~~~
        || {numbers[3]} || {numbers[4]} || {numbers[5]} ||
        ~~~~~~~~~~~~~~~~~
        || {numbers[6]} || {numbers[7]} || {numbers[8]} ||
        ~~~~~~~~~~~~~~~~~
    ''')

def win():
    if numbers[0] == "X" and numbers[1] == "X" and numbers[2] == "X":
        print("Player X wins!")
        breaking = True
    elif numbers[0] == "O" and numbers[1] == "O" and numbers[2] == "O":
        print("Player O wins!")
        breaking = True
    elif numbers[0] == "X" and numbers[4] == "X" and numbers[8] == "X":
        print("Player X wins!")
        breaking = True
    elif numbers[0] == "O" and numbers[4] == "O" and numbers[8] == "O":
        print("Player O wins!")
        breaking = True
    elif numbers[3] == "X" and numbers[4] == "X" and numbers[5] == "X":
        print("Player X wins!")
        breaking = True
    elif numbers[3] == "O" and numbers[4] == "O" and numbers[5] == "O":
        print("Player O wins!")
        breaking = True
    elif numbers[6] == "X" and numbers[4] == "X" and numbers[2] == "X":
        print("Player X wins!")
        breaking = True
    elif numbers[6] == "O" and numbers[4] == "O" and numbers[2] == "O":
        print("Player O wins!")
        breaking = True
    elif numbers[6] == "X" and numbers[7] == "X" and numbers[8] == "X":
        print("Player X wins!")
        breaking = True
    elif numbers[6] == "O" and numbers[7] == "O" and numbers[8] == "O":
        print("Player O wins!")
        breaking = True
    elif numbers[0] == "X" and numbers[3] == "X" and numbers[6] == "X":
        print("Player X wins!")
        breaking = True
    elif numbers[0] == "O" and numbers[3] == "O" and numbers[6] == "O":
        print("Player O wins!")
        breaking = True
    elif numbers[1] == "X" and numbers[4] == "X" and numbers[7] == "X":
        print("Player X wins!")
        breaking = True
    elif numbers[1] == "O" and numbers[4] == "O" and numbers[7] == "O":
        print("Player O wins!")
        breaking = True
    elif numbers[2] == "X" and numbers[5] == "X" and numbers[8] == "X":
        print("Player X wins!")
        breaking = True
    elif numbers[2] == "O" and numbers[5] == "O" and numbers[8] == "O":
        print("Player O wins!")
        breaking = True
    else:
        breaking = False
    return breaking



playing = True
while playing:
    numbers = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    gui()
    for i in range(1,10):
        if i % 2 == True:
            whom = "O"        
        else:
            whom = "X"
        while True:
            where = int(input(f"{whom}, where would you like to place your piece (1-9): "))
            if numbers[where-1] == "_":
                numbers[where-1] = whom
                break
            else:
                print("Sorry, this spot has already been taken. Choose a different one.")
                continue
        gui()
        breaking = win()
        if breaking:
            break
    again = input("Play again? (y/n): ").lower().strip()
    if again == "n":
        playing = False