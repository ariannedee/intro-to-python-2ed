"""
Provide a countdown for X seconds, then print "Happy New Year! 🎉"
"""
from time import sleep

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        seconds -= 1
        sleep(1)
    print('Happy New Year! 🎉')


countdown(10)
