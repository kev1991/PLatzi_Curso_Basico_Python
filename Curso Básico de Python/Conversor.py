def converter (type_pesos, dollar_value):
    pesos = input("How many "+ type_pesos + " pesos do you have?: ")
    pesos = float(pesos)
    dollars = pesos / dollar_value
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print ("You have $" + dollars + " dollars")

menu = """
Welcome to currency converter 💲

     #1 Colombian pesos
     #2 Argentine pesos
     #3 Mexican pesos

     Choose an option: 
"""
option = input(menu)

if option == "1":
    converter ("Colombias", 3875)
elif option == "2":
    converter ("Argentine", 65)
elif option == "3":
    converter ("Mexican", 24)
else:
    print("Please enter one correct option ")