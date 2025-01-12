sum_ = 0

with open('data/input.txt') as file:
    for line in file.readlines():
        sum_ += float(line.strip())

print(sum_)
