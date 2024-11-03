def add(a, b):
    a = float(a)
    b = float(b)
    return round(a + b, 8)


print(add(1, 2))
print(add(1.1, 2.2))
print(add('1', '2'))
