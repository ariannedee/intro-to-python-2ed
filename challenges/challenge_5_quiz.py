"""
Quiz game

User will try to get all the answers (e.g. countries that start with V)
If they give up and quit, print the ones that were missed
"""

answers = [
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
]

category = 'Country that starts with V'

guessed = []

# 4 left
guess = input(f"Enter a {category.lower()} (q to quit): ")

# Correct!
# Already guessed
# Try again

# Great job!
# You missed: a, b, c, d
