from random import randint

def x():

    random_number = randint(1, 20)
    tries = 0
    
    while True:
        guess = int(input("Tahmin: "))
        tries += 1

        if guess < random_number:
            print("Katta son")

        elif guess > random_number:
            print('Kichik son')

        elif guess == random_number:
            print(f"{tries} ta urinishda topdingiz")
            break

x()

