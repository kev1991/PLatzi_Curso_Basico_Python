import random


def password_generator():
    capital_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    symbols = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']


    characters = capital_letter + lowercase + number + symbols

    password = []

    for i in range(15):
        random_character =random.choice(characters)
        password.append(random_character)

    password = ''.join(password)
    return password

def kev():
    password = password_generator()
    print ("your new password is :" + password)


if __name__ == "__main__":
    kev()