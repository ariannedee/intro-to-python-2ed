"""
Calculate the area of a triangle using Heron's formula
"""
import math

a = 3
b = 4
c = 5

s = (a + b + c) / 2  # superperimeter
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(round(area, 2))
