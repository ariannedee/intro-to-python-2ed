"""
Quiz game

User will try to get all the answers (e.g. countries that start with V)
If they give up and quit, print the ones that were missed
"""

category = 'Country that starts with V'
answers = {
    'Vanuatu': [],
    'Vatican City': ['Vatican'],
    'Venezuela': [],
    'Vietnam': [],
}


def get_answer(guess):
    for name, other_options in answers.items():
        if guess.lower() == name.lower():
            return name
        for option in other_options:
            if guess.lower() == option.lower():
                return name


def check_guess(guess, guessed, answers_left):
    answer = get_answer(guess)
    if answer in guessed:
        return 'Already guessed'
    elif answer in answers_left:
        guessed.append(answer)
        answers_left.remove(answer)
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
    answers_left = list(answers.keys())

    while len(answers_left) > 0:
        print(f"{len(answers_left)} left")

        guess = input(f"Enter a {category.lower()} (q to quit): ")
        if guess == 'q':
            break
        print(check_guess(guess, guessed, answers_left))

    print(get_result(answers_left))


if __name__ == '__main__':
    play_game()
