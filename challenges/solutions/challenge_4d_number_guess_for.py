"""
Number guessing game

You have 4 tries to guess a number between 1 and 20.
"""
import random


def play_game(num_guesses):
    answer = random.randint(1, 20)

    print("I'm thinking of a number between 1 and 20")

    for i in range(num_guesses):
        num_guesses_left = num_guesses - i
        suffix = '' if num_guesses_left == 1 else 'es'
        print(f"You have {num_guesses_left} guess{suffix} left")

        guess = int(input("Make a guess: "))

        if answer == guess:
            print('Got it!')
            return
        elif answer > guess:
            print('Higher')
        elif answer < guess:
            print('Lower')

    print(f"It was {answer}")


play_game(4)