import time
import random


def time_target(num_seconds):
    input(f"{num_seconds}s test. Hit enter to start and stop. ")
    start = time.time()
    input("Hit enter to stop ")
    stop = time.time()

    duration = stop - start
    results = f"""
{round(duration, 3)}s
You were {round(duration - num_seconds, 3)}s off
"""
    print(results)

target_seconds = random.randint(2, 5)

time_target(target_seconds)
time_target(target_seconds)
time_target(target_seconds)