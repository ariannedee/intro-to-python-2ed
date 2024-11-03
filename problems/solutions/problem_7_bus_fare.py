"""
Determine how much to pay for the bus

Children 12 and under are free
People age 13-17, 65+, and students pay half price
"""
age = int(input("Enter your age: "))
student = input("Are you a student? (y or n): ").lower().startswith('y')

full_fare = 3.50

if age <= 12:
    your_fare = 0
elif age < 18 or age >= 65 or student:
    your_fare = full_fare / 2
else:
    your_fare = full_fare

print(f"Your fare is ${your_fare:.2f}")