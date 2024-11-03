"""
Simulate rolling 2 dice
"""
import random
die_1 = random.randint(1, 6)
die_2 = random.randint(1, 6)

print(f"You rolled a {die_1} and {die_2} (total: {die_1 + die_2})")
