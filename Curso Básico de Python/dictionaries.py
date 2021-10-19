def kev():
    my_dictionari = {
        "key1": 1,
        "key2": 2,
        "key3": 3
    }
    # print(my_dictionari ["key1"])
    # print(my_dictionari ["key2"])
    # print(my_dictionari ["key3"])

    countries_populetion ={
        "Argentina": 44938712,
        "Brazil": 210147125,
        "Colombia": 50372424 
    }
    # print("The population in Argentina is ") 
    # print(countries_populetion["Argentina"] )

    # for country in countries_populetion.keys():
    #     print (country)

    # for populetion in countries_populetion.values():
    #     print (populetion)

    for country, populetion in countries_populetion.items():
        print ("The population in " + country + " is " + str (populetion) + " inhabitants")

if __name__ == "__main__":
    kev()