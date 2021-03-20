import random
def compputer_guess(x):
    low=1
    high=x
    feeback=''

    while feeback != 'c':
        if low!=high:
            guess_number = random.randint(low, high)

        else:
            guess_number = low

        feeback=input(f"Is {guess_number} is too high (H) or too low (L) or correct (C)??")
        if feeback=='h':
            high= guess_number-1

        elif feeback=='l':
            low= guess_number+1
    print(f"Yay 'computer guessed the number {guess_number} correctly")
compputer_guess(100)
