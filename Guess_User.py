import random

def guess(x):
    random_number = int(input(f"Input a number of your choice between 1 and {x}: "))
    guess = 0
    while guess != random_number:
        guess = random.randint(1, x)
        if guess < random_number:
            print(f"Sorry, {guess} is too low. try again!")
        if guess > random_number:
            print(f"Sorry, {guess} too high. try again!")
    print(f"YAY, Congrats {guess} is the correct number.")

guess(15)