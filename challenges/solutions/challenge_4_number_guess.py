"""
Number guessing game

You have 3 tries to guess a number between 1 and 20.
"""
import random


def play_game():
    answer = random.randint(1, 20)

    print("I'm thinking of a number between 1 and 20")

    guess = int(input("Make a guess: "))

    if answer == guess:
        print('Got it!')
        exit()
    elif answer > guess:
        print('Higher')
    elif answer < guess:
        print('Lower')

    guess = int(input("Make a guess: "))

    if answer == guess:
        print('Got it!')
        exit()
    elif answer > guess:
        print('Higher')
    elif answer < guess:
        print('Lower')

    guess = int(input("Make a guess: "))

    if answer == guess:
        print('Got it!')
        exit()
    elif answer > guess:
        print('Higher')
    elif answer < guess:
        print('Lower')

    print(f"It was {answer}")


play_game()