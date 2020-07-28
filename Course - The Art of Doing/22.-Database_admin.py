#!/usr/bin python3

login_info = {
    "superadmin":"admin123",
    "alice22":"boblove",
    "bob23":"gimmeyourprimenumbers",
    "stealthy":"subtle",
    "1337":"haxx0r",
    }

print("Welcome to the Database Admin App!")
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in login_info.keys() and password == login_info[username]:
        print("Hello " + username + ". You have successfully logged in!")
        if "superadmin" in username:
            print("\nHere is the current user database:")
            for key, value in login_info.items():
                print("Username: " + key + "\t\t\tPassword: " + value)
            break
        else:
            print("Your current password is " + str(login_info[username]))
    else:
        print("Sorry, you have entered wrong credentials. Please make sure you type correctly both username and password")
        continue
    password_change_question = input("Would you like to change it? ")
    if password_change_question.startswith("y"):
        while True:
            new_password = input("Please enter your new password: ")
            if len(new_password) < 8:
                print("Please, enter a password of at least 8 characters")
                continue
            else:
                login_info[username] = new_password
                break
        print("\n" + username + ", your new password is " + login_info[username])
    else:
        print("You are now logged off!")
    break



