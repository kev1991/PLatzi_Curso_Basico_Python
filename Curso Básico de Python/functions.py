# def print_message():
#     print("Special message")
#     print("I am lear use functions")

# print_message()
# print_message()
# print_message()

def conversation(message):
    print ("Hi")
    print ("How's it going?")
    print (message)
    print ("Goodbye")


option = input("Choose one option (1, 2, 3)")
if option == "1":
    conversation("you chose option 1")
elif option == "2":
    conversation("you chose option 2")
elif option == "3":
    conversation("you chose option 3")
else:
    print ("Write one correct option")