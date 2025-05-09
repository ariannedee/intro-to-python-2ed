"""
Quiz game

User will try to get all the answers (e.g. countries that start with V)
If they give up and quit, print the ones that were missed
"""

with open('data/C_elements.txt') as file:
    category = file.readline().strip()
    answers = file.read().split('\n')

guessed = []

while True:
    num_left = len(answers)
    if num_left == 0:
        print('Great job!')
        break
    print(f"{num_left} left")

    guess = input(f"{category} (q to quit): ")
    if guess.lower() == 'q':
        missed = ', '.join(answers)
        print('You missed: ' + missed)
        break

    if guess in guessed:
        print('Already guessed')
    elif guess in answers:
        print('Correct!')
        guessed.append(guess)
        answers.remove(guess)
    else:
        print('Try again')
