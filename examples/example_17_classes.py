class MyClass:
    def __init__(self, attr1='hello'):
        self.attr1 = attr1
        self.attr2 = 'B'

    def a_method(self):
        print(f'Called a_method on {self}')

    def __str__(self):
        return f'Instance ({self.attr1}, {self.attr2})'


class Horse:
    def __init__(self, colour, age):
        self.age = age
        self.colour = colour

    def trot(self):
        print('clop clop clop clop')

    def __str__(self):
        return f'{self.colour.capitalize()} horse, age {self.age}'


obj = MyClass()  # Creating instances from classes
horse1 = Horse('black', 4)  # Calls __init__

print(obj)  # Printing an object calls __str__
print(horse1)

print(type(obj))  # Returns the class
print(type(horse1))

obj.a_method()  # Call methods
horse1.trot()

print(obj.attr1)  # Access attributes
print(horse1.colour)
