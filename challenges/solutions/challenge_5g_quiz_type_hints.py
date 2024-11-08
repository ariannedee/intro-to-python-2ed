"""
Quiz game

User will try to get all the answers (e.g. countries that start with V)
If they give up and quit, print the ones that were missed
"""

v_country_category: str = 'Country that starts with V'
v_countries: list[str] = [
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
]


def check_guess(guess: str, guessed: list[str], answers_left: list[str]) -> str:
    if guess in guessed:
        return 'Already guessed'
    elif guess in answers_left:
        guessed.append(guess)
        answers_left.remove(guess)
        return 'Correct!'
    else:
        return 'Try again'


def get_result(answers_left: list[str]) -> str:
    if len(answers_left) == 0:
        return 'Great job!'
    else:
        missed = ', '.join(answers_left)
        return 'You missed: ' + missed


def play_game(category: str, answers: list[str]) -> None:
    guessed = []
    answers_left = answers.copy()

    while len(answers_left) > 0:
        print(f"{len(answers_left)} left")

        guess = input(f"Enter a {category.lower()} (q to quit): ")
        if guess == 'q':
            break
        print(check_guess(guess, guessed, answers_left))

    print(get_result(answers_left))


if __name__ == '__main__':
    play_game(v_country_category, v_countries)
