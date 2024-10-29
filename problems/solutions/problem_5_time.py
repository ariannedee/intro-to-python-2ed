"""
Print the elapsed time
"""
from time import time

start = time()
input("Press enter to START the timer: ")
input("Press enter to STOP the timer: ")
stop = time()

print(f"{round(stop - start, 2)}s elapsed")
