# Optional parameters
def add(a, b, precision=8):
    a = float(a)
    b = float(b)
    return round(a + b, precision)


print(add(1.1, 2.2))
print(add('1.1', '2.2', 20))
print(add('1.1', '2.2', None))


# Keyword arguments
def add(a, b):
    a = float(a)
    b = float(b)
    return round(a + b, 8)


print(add(1, 2))          # Positional args
print(add(a=1.1, b=2.2))  # Keyword args (also called kwargs)
print(add('1', b='2'))    # Positional must come before keyword
print(add(b='1', a='2'))  # Order doesn't matter for kwargs


# Docstrings
def add(a, b):
    """Add two numbers"""
    a = float(a)
    b = float(b)
    return round(a + b, 8)


print(add(1, 2))
help(add)


# Nested functions
def add(a, b):
    def convert(n):  # converts to int if no decimal, else float
        if isinstance(n, str):
            if n.isnumeric():
                return int(n)
            return float(n)
        return n

    a = convert(a)
    b = convert(b)
    return round(a + b, 8)


print(add(1, 2))
print(add(1.1, 2.2))
print(add('1', '2'))


# *args and **kwargs
def add(a, b):
    a = float(a)
    b = float(b)
    return round(a + b, 8)


print(add(1, 2))
print(add(a=1.1, b=2.2))
print(add('1', b='2'))

args = [-1, -2]
kwargs = {'a': '9', 'b': '0.9'}

print(add(*args))  # add(-1, -2)
print(add(**kwargs))  # add(a='9', b='0.9')
