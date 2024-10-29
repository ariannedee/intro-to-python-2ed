"""
Simulate rolling 2 dice
"""
import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

print(f"You rolled a {die1} and {die2} (total: {die1 + die2})")
