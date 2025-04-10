# Creating lists
letters = ['A', 'B', 'C', 'D']
lowercase = list('abcd')  # ['a', 'b', 'c', 'd']
empty = []
also_empty = list()

# Indexing and slicing
print(letters[0])     # 'A'
print(letters[-1])    # 'D'
print(letters[1:3])   # ['B', 'C']
print(letters[:2])    # ['A', 'B']
print(letters[2:])    # ['C', 'D']
print(letters[::-1])  # ['D', 'C', 'B', 'A']

# Length and containment
print(len(letters))    # Get the length of a list
print('A' in letters)  # Check if an item is in a list

# Adding, removing, and updating
letters = ['A', 'B', 'C', 'D']

letters[0] = 'a'                 # Update an item by index
del letters[1]                   # Delete an item by index
letters.append('E')              # Add an item to end of list
letters.insert(1, 'B')           # Add an item to an index
letters.extend(['A', 'B', 'C'])  # Add each item from a sequence to the end of the list
letters.remove('B')              # Remove first instance of item, raise ValueError if not found
print(letters)

# More list methods
print(letters.count('C'))  # Returns 2, lists can have duplicates
print(letters.pop())       # Removes and returns the last item
print(letters.index('A'))  # Return the index of the item if found, raise ValueError if not found

letters.reverse()  # Returns None, but reverses the original list
print(letters)

letters.sort()     # Returns None, but sorts the original list, raises TypeError if it can't be sorted
print(letters)

# Nested lists can be used for matrices
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matrix[1][0] = 1000  # Change 4 to 1000
print(matrix)
