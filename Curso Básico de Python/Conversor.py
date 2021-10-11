menu = """
Welcome to currency converter 💲

     #1 Colombian pesos
     #2 Argentine pesos
     #3 Mexican pesos

     Choose an option: 
"""
option = input(menu)

if option == "1":
    pesos = input("How many Colombias pesos do you have?: ")
    pesos = float(pesos)
    dollar_value = 3875
    dollars = pesos / dollar_value
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print ("You have $" + dollars + " dollars")

elif option == "2":
    pesos = input("How many Argentine pesos do you have?: ")
    pesos = float(pesos)
    dollar_value = 65
    dollars = pesos / dollar_value
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print ("You have $" + dollars + " dollars")

elif option == "3":
    pesos = input("How many Mexican pesos do you have?: ")
    pesos = float(pesos)
    dollar_value = 24
    dollars = pesos / dollar_value
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print ("You have $" + dollars + " dollars")
else:
    print("Please enter one correct option ")