# Use range() to loop through a sequence of integers
for i in range(10):
    print(i)
print()

for i in range(10, 20):
    print(i)
print()

for i in range(10, 20, 2):
    print(i)
print()

# ------------------------------

primes = [2, 3, 5, 7, 11, 13]
# Can loop over lists
for prime in primes:
    print(prime)

# Create a new list from an existing one
prime_squares = []
for prime in primes:
    prime_squares.append(prime ** 2)
print(prime_squares)


# If you need to know the index, use enumerate()
for i, prime in enumerate(primes):
    print(f"{i}: {prime} squared is {prime ** 2}")


# sorted() and reversed() can be used when looping over sequences
for prime in reversed(primes):
    print(f"{prime} squared is {prime ** 2}")
