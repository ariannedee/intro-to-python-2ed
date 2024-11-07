"""
Quiz game

User will try to get all the answers (e.g. countries that start with V)
If they give up and quit, print the ones that were missed
"""


def play_game(category, answers):
    def check_guess(guess):
        if guess in guessed:
            return 'Already guessed'
        elif guess in answers_left:
            guessed.append(guess)
            answers_left.remove(guess)
            return 'Correct!'
        else:
            return 'Try again'

    def get_result():
        if len(answers_left) == 0:
            return 'Great job!'
        else:
            missed = ', '.join(answers_left)
            return 'You missed: ' + missed

    guessed = []
    answers_left = answers.copy()

    while len(answers_left) > 0:
        print(f"{len(answers_left)} left")

        user_guess = input(f"Enter a {category.lower()} (q to quit): ")
        if user_guess == 'q':
            break
        print(check_guess(user_guess))

    print(get_result())


if __name__ == '__main__':
    v_country_category = 'Country that starts with V'
    v_countries = [
        'Vanuatu',
        'Vatican City',
        'Venezuela',
        'Vietnam',
    ]
    play_game(answers=v_countries, category=v_country_category)
