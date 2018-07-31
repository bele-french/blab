import random
n = random.randint(1,99)
guess = int(input("What is your guess?"))
while n != guess:
    if guess < n:
        print("Guess is too low")
        guess = int(input("Guess again"))
    elif guess > n:
        print("Guess is too high")
        guess = int(input("Guess again"))

    else:
        print("Guessed it")

