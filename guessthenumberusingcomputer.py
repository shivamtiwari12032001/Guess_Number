import random

def guess(x):
    guess_number=0
    random_number=random.randint(1,x)
    while(guess_number!=random_number):
        guess_number=int(input(f"Enter the number netween 1 and {x}: "))
        if(guess_number<random_number):
            print("Sorry guess again, too less ")
        elif guess_number>random_number:
            print("Sorry guess again, too high ")
        else:
            print(f"yay congrats you guessed the random number {random_number} correctly")

guess(10)