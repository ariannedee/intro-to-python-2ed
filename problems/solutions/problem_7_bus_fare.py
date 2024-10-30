"""
Determine how much to pay for the bus

Children 12 and under are free
People 13-17 and 65+ are discounted

All fares are halved during non-peak hours
"""
PEAK_HOURS = True

discount_fare = 2.00
full_fare = 3.50

def bus_fare(age):
    if age <= 12:
        fare = 0
    elif age <= 17 or age >=65:
        fare = discount_fare
    else:
        fare = full_fare

    if not PEAK_HOURS:
        fare = fare / 2

    return fare


total = (bus_fare(12) +
         bus_fare(17) +
         bus_fare(37) +
         bus_fare(65))

# Should be $7.50 during peak hours
# and $3.75 during non-peak hours
print(f"You need ${total:.2f}")