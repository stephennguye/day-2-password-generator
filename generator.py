import string
import random

character_list = ""

def character_options():
    print("Choose the character types for the password")
    print('''
          1. Letters
          2. Digits
          3. Special characters
          4. Done''')

def choose_character_types():
    global character_list
    while True:
        number = int(input("Choose a number (1-4): "))

        if number == 1:
            character_list += string.ascii_letters
        elif number == 2:
            character_list += string.digits
        elif number == 3:
            character_list += string.punctuation
        elif number == 4:
            break
        else:
            print("Invalid number bro. Try again")

def password_generation():
    if not character_list:
        print("You must choose at least one character type")
        return
    else:
        password = []
        for i in range(password_length):
            randomchar = random.choice(character_list)
            password.append(randomchar)
        print(f"Done! Your password is {''.join(password)}")

if __name__ == "__main__":
    password_length = int(input("Enter the length of your desired password: "))
    character_options()
    choose_character_types()
    password_generation()
    