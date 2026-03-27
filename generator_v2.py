import string
import random

def split_password_length(password_length):
    while True: 
        try:
            if password_length < 8:
                print("Password length must be from 8 characters above. Try again bro!")
                password_length = int(input("Enter your password length again bro: "))
            else:
                break

        except:
            password_length = int(input("Bro you're wrong! Enter numbers only (>=8): "))

    first_half = round(password_length * 30 / 100)
    other_half = round(password_length * 20 / 100)

    return first_half, other_half


def assign_character_types(first_half, other_half, combination):
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    for x in range(first_half):
        combination.append(s1[x])
        combination.append(s2[x])
    
    for y in range(other_half):
        combination.append(s3[y])
        combination.append(s4[y])

    return combination

def shuffle_password(combination):
    random.shuffle(combination)
    return combination


if __name__ == "__main__":
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)
    combination = []

    password_length = int(input("Enter your desired password length: "))

    first_half, other_half = split_password_length(password_length)
    combination = assign_character_types(first_half, other_half, combination)
    password = "".join(shuffle_password(combination))
    print(f"Your password is {password}")
