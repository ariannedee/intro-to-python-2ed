"""
Quiz game

User will try to get all the answers (e.g. countries that start with V)
If they give up and quit, print the ones that were missed
"""

v_country_category = 'Country that starts with V'
v_countries = [
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
]


class Game:
    def __init__(self, category, answers):
        self.prompt = f"Enter a {category.lower()} (q to quit): "
        self.answers_left = answers.copy()
        self.guessed = []

    def check_guess(self, guess):
        if guess in self.guessed:
            return 'Already guessed'
        elif guess in self.answers_left:
            self.guessed.append(guess)
            self.answers_left.remove(guess)
            return 'Correct!'
        else:
            return 'Try again'

    def get_result(self):
        if len(self.answers_left) == 0:
            return 'Great job!'
        else:
            missed = ', '.join(self.answers_left)
            return 'You missed: ' + missed

    def play_game(self):
        while len(self.answers_left) > 0:
            print(f"{len(self.answers_left)} left")

            guess = input(self.prompt)
            if guess == 'q':
                break
            print(self.check_guess(guess))

        print(self.get_result())


if __name__ == '__main__':
    g = Game(v_country_category, v_countries)
    g.play_game()
