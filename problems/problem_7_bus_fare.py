"""
Determine how much to pay for the bus

Children 12 and under are free
People age 13-17, 65+, and students pay half price
"""
age = int(input("Enter your age: "))
student = input("Are you a student? (y or n): ")

full_fare = 3.50

your_fare = None

print(f"Your fare is ${your_fare}")