temp = -12

if temp <= 0:    # Must have 1
    print("It's freezing")
elif temp < 18:  # Can have 0+
    print("It's cold")
else:            # Can have 0 or 1
    print("It's not cold")

# ------------------------------

name = input("What's your name? ")

if name:  # No input (empty string)
    print("Hello " + name)
else:
    print("Hello, world")

# ------------------------------

cost = 0

if cost is None:  # If this was "if not cost:", it would catch 0 and False
    print("Set a cost")
else:
    print(f"It cost ${cost}")
