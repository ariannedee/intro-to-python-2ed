"""
Mad Libs
"""
colour = input("Colour: ").strip().upper()
adjective = input("Adjective: ").strip().upper()

text = f"""
Roses are {colour},
Violets are blue,
Sugar is {adjective},
And so are you!
"""

print(text)
