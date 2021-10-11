pesos = input("How many Colombias pesos do you have?: ")
pesos = float(pesos)
dollar_value = 3875
dollars = pesos / dollar_value
dollars = round(dollars, 2)
dollars = str(dollars)
print ("You have $" + dollars + " dollars")