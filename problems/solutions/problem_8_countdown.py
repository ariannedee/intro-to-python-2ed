"""
Provide a countdown for X seconds, then print "Happy New Year! 🎉"
"""
from time import sleep


def countdown(seconds):
    while seconds > 0:
        print(seconds)
        sleep(1)
        seconds -= 1
    print('Happy New Year! 🎉')


countdown(5)
