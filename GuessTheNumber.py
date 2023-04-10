import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Tente novamente. Muito baixo")
        else:
            print("Tente novamente. Muito alto")

    print(f"Uhull, você acertou o número {random_number}!")

guess(10)