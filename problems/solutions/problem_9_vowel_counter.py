"""
Print how many vowels that an input word contains.
"""

word = input("Type a word: ")

num_vowels = 0
for char in word.lower():
    if char in 'aeiou':
        num_vowels += 1

print(f'There are {num_vowels} vowels in "{word}"')
