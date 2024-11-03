# Indexing and slicing
letters = ['A', 'B', 'C', 'D']

print(letters[0])     # 'A'
print(letters[-1])    # 'D'
print(letters[1:3])   # ['B', 'C']
print(letters[:2])    # ['A', 'B']
print(letters[2:])    # ['C', 'D']
print(letters[::-1])  # ['D', 'C', 'B', 'A']
print()

# ------------------------------

# Adding, removing, and updating
languages = ['English', 'French', 'Tagalog', 'Mandarin']

languages[1] = 'Français'
languages.append('Icelandic')    # Adds item to end of list
languages.insert(1, 'Urdu')      # Adds item to list at index
languages.remove('English')      # Remove first instance of item, raise error if not found
print(languages)

# ------------------------------

# More list methods
letters.insert(1, True)    # Lists can hold any type of data
letters.extend([1, 2, 3])  # Add contents of another sequence to the end
print(letters)
print(letters.count(1))  # Remember, 1 == True

letters.reverse()  # Some methods return None, but alter the list
print(letters)

letters.sort()
print(letters)


# Nested lists can be used for matrices
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matrix[1][0] = 1000
print(matrix)
