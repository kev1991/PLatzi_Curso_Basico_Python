import random


def kev():
    randon_number = random.randint(1, 100)
    selected_number = int(input("Choos one number from 1 to 100: "))
    while selected_number != randon_number:
        if selected_number < randon_number:
            print("look a bigger number ")
        else:
            print("look a smaller number ")
        selected_number = int(input("Choos other number: "))
    print("¡you won!")


if __name__ == "__main__":
    kev()

