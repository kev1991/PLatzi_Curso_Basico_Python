dollars = input("Hoy many Dollars do you have?: ")
dollars = float(dollars)
Colombias_pesos = 3758.89

pesos = (dollars * Colombias_pesos) / 1
pesos = round(pesos, 2)
pesos = str(pesos)
print ("You have $" + pesos + " pesos Colombianaos")
