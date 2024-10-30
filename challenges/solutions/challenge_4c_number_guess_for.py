"""
Number guessing game

You have 4 tries to guess a number between 1 and 20.
"""
import random


answer = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")

guess = int(input("Make a guess: "))
if answer == guess:
    print('Correct!')
    exit()
elif answer > guess:
    print('Higher')
else:
    print('Lower')

guess = int(input("Make a guess: "))
if answer == guess:
    print('Correct!')
    exit()
elif answer > guess:
    print('Higher')
else:
    print('Lower')

guess = int(input("Make a guess: "))
if answer == guess:
    print('Correct!')
    exit()
elif answer > guess:
    print('Higher')
else:
    print('Lower')

guess = int(input("Make a guess: "))
if answer == guess:
    print('Correct!')
    exit()
elif answer > guess:
    print('Higher')
else:
    print('Lower')

print(f'The answer was {answer}')