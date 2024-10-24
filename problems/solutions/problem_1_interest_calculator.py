"""
Calculate the amount gained on an investment with compounded interest
"""
principal = 10_000  # initial investment
rate = 0.02         # annual interest rate
n = 1               # number of times the interest compounds per year
years = 10

amount = principal * (1 + rate / n) ** (n * years)
total_interest = amount - principal

print(round(total_interest, 2))
