import string
import random

def character_options():
    print('''Choose the character types for the password
            1. Letters
            2. Digits
            3. Special characters
            4. Done''')

def choose_character_types():
    character_list = ""

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
    
    return character_list

def password_generation(character_list, password_length):
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
    character_list = choose_character_types()
    password = password_generation(character_list, password_length)
    