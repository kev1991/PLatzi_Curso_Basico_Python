def palindrome(word):
    word = word.replace(" ","")
    word = word.lower()
    inverted_word = word[::-1]
    if word == inverted_word:
        return True
    else:
        return False



def run():
    word = input ("Write one word: ")
    is_palindrome = palindrome(word) 
    if is_palindrome == True:
        print("Is palindrome")
    else:
        print ("Isn't palindrome")


if __name__ == "__main__":
    run()