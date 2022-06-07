import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, it's too low. guess again.")
        if guess > random_number:
            print("Sorry, it's too high. guess again.")
    print(f"Yay, Congrats you guessed the {random_number} correct.")


guess(10)
