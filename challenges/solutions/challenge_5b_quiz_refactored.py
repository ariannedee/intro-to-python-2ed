"""
Quiz game

User will try to get all the answers (e.g. countries that start with V)
If they give up and quit, print the ones that were missed
"""

category = 'Country that starts with V'
answers = [
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
]


def check_guess(guess, guessed, answers_left):
    if guess in guessed:
        return 'Already guessed'
    elif guess in answers_left:
        guessed.append(guess)
        answers_left.remove(guess)
        return 'Correct!'
    else:
        return 'Try again'


def get_result(answers_left):
    if len(answers_left) == 0:
        return 'Great job!'
    else:
        missed = ', '.join(answers_left)
        return 'You missed: ' + missed


def play_game():
    guessed = []
    answers_left = answers.copy()
    print(answers_left)

    while len(answers_left) > 0:
        print(f"{len(answers_left)} left")

        guess = input(f"Enter a {category.lower()} (q to quit): ")
        if guess == 'q':
            break
        print(check_guess(guess, guessed, answers_left))

    print(get_result(answers_left))


if __name__ == '__main__':
    play_game()
