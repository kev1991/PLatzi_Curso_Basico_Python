def run():
    LIMIT = 1024

    counter = 0
    power_2 =2 ** counter
    while power_2 <LIMIT:
        print("2 reised to " + str(counter) +
         " is equal to: " + str(power_2))
        counter = counter + 1
        power_2 = 2 ** counter


if __name__ == "__main__":
     run()
