"""
Time target game
"""
import time
from random import randint


def time_game(target_seconds):
    input(f"{target_seconds}s test. Hit ENTER to start ")
    start = time.time()

    input("Hit ENTER to stop ")
    end = time.time()

    duration = end - start
    difference = abs(target_seconds - duration)

    print(f"{duration:.3}s")
    print(f"You were {difference:.3}s off")

seconds = randint(2, 5)
time_game(seconds)
time_game(seconds)
time_game(seconds)