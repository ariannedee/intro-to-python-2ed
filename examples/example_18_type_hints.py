# functions
def add(n1: int, n2: int | float = 0) -> int | float:
    return n1 + n2


# variables
total: int = add(12, 13)

# containers
totals: list[int] = [12, 13, 14]

# multiple options
total_2: int | float = add(1.2, 1.3)
