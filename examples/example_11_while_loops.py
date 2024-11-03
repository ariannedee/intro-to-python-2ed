x = 0
while x <= 10:  # Stop looping when condition is False
    print(x)
    x += 1

# ------------------------------

x = 0
while True:
    print(x)
    if x == 10:
        break  # Stop looping when break is reached
    x += 1

# ------------------------------

x = -1
while True:
    x += 1
    if x % 2 == 1:
        continue  # Stop the current loop and continue on to the next loop
    print(x)
    if x == 10:
        break
