"""
Number guessing game

You have 3 tries to guess a number between 1 and 20.
"""
import random


answer = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")

guess = int(input("Make a guess: "))
