# DICTIONARIES
my_dict = {'A': 1, 'B': 2}

my_dict['A']        # Get item by key
my_dict['C'] = 3    # Add a new item
my_dict['A'] = 100  # Update item

my_dict.get('A')         # Returns item by key
my_dict.get('D')         # Returns None if key doesn't exist
my_dict.get('D', 'N/A')  # Returns a default value if key doesn't exist (e.g. N/A)

'A' in my_dict         # Check if key is in dict
3 in my_dict.values()  # Check if value is in dict

for key in my_dict:  # For-loops loop over keys by default
    print(key)


for key, value in my_dict.items():  # Access key and value in a for-loop
    print(f"{key}: {value}")


# TUPLES
my_tuple = (1, 2)

my_tuple[-1]  # Get item by index

paris = (33.66, -95.55)  # Useful if order and contents shouldn't change
lat, lon = paris         # Unpack items into variables
london = 42.98, -81.25   # Pack items into tuples (parentheses not needed)

# Potential uses
isinstance(1, (int, float))  # Passing multiple items to a single argument
div, mod = divmod(11, 2)     # Returning multiple items from a function
for key, value in my_dict.items():  # key, value is actually unpacking a tuple
    print(f"{key}: {value}")

# SETS
my_set = {3, 2, 1, 2, 3}

assert len(my_set) == 3  # Removes duplicates
print(my_set)            # prints {1, 2, 3} - doesn't retain order

set(['item1', 'item2', 'item1', 'item3'])  # Find unique items from list

primes = {2, 3, 5, 7}
odd = {1, 3, 5, 7}

# Set operations
intersection = primes & odd          # Items in both sets
union = primes | odd                 # Items in either set
difference = primes - odd            # Items in one set but not the other
symmetric_difference = primes ^ odd  # Items in either set but not both
