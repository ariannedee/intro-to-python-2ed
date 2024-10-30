answers = [
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
]


def make_guess(prompt):
    return input(prompt + ' (q to quit): ').strip()

def game_over(guessed):
    return len(answers) == len(guessed)

def missed_answers(guessed):
    missed = []
    for answer in answers:
        if answer not in guessed:
            missed.append(answer)
    return missed

def answers_left(guessed):
    return len(answers) - len(guessed)

def play_game():
    correct = []
    while not game_over(correct):
        print(f"{answers_left(correct)} left")
        guess = make_guess('Countries that start with V')
        if guess.lower() == 'q':
            print('\nYou missed: ' + ', '.join(missed_answers(correct)))
            return
        elif guess in correct:
            print('  Already guessed')
        elif guess in answers:
            print('  Correct!')
            correct.append(guess)
        else:
            print('  Try again')
    print('Great job!')


play_game()
