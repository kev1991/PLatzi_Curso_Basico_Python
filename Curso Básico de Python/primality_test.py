def is_primalaty(number):
    counter = 0

    for i in range(1, number + 1):
        if i == 1 or i == number: 
            continue
        if number % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False
        pass



def kev():
    number = int(input("Write one number: "))
    if is_primalaty(number):
        print("is primality") 
    else:
        print("is not primality")


if __name__== "__main__":
    kev()