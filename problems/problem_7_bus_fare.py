"""
Determine how much to pay for the bus

Children 12 and under are free
People 13-17 and 65+ are discounted

All fares are halved during non-peak hours
"""
PEAK_HOURS = False

discount_fare = 2.00
full_fare = 3.50

def bus_fare(age):
    return 0


total = (bus_fare(12) +
         bus_fare(17) +
         bus_fare(37) +
         bus_fare(65))

# Should be $7.50 during peak hours
# and $3.75 during non-peak hours
print(f"You need ${total:.2f}")