v_countries = [
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
]

guessed = []

while True:
    num_left = len(v_countries) - len(guessed)
    if num_left == 0:
        print('Great job!')
        break

    print(f"{num_left} left")
    guess = input("Enter a country that starts with V (q to quit): ")

    if guess.lower() == 'q':
        missed = list(v_countries)
        for got in guessed:
            missed.remove(got)
        print(f"\n  You missed: {', '.join(v_countries)}")
        break
    elif guess in guessed:
        print('  Already guessed')
    elif guess in v_countries:
        print('  Correct!')
        v_countries.remove(guess)
    else:
        print('  Try again')
