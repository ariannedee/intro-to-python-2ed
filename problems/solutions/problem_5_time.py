"""
Print the elapsed time
"""
import time

input("Press enter to START the timer: ")
start = time.time()
input("Press enter to STOP the timer: ")
end = time.time()

print(f"{end - start}s elapsed")
