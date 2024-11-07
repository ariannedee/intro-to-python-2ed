from challenge_5b_quiz_refactored import check_guess, get_result


def test_check_guess():
    assert check_guess('A', guessed=['A'], answers_left=['A']) == 'Already guessed'
    assert check_guess('A', guessed=['B'], answers_left=['A']) == 'Correct!'
    assert check_guess('C', guessed=['A'], answers_left=['B']) == 'Try again'


def test_check_guess_case_sensitive():
    assert check_guess('a', guessed=[], answers_left=['A']) == 'Try again'
    assert check_guess('a', guessed=['A'], answers_left=['a']) == 'Correct!'


def test_get_result():
    assert get_result([]) == 'Great job!'
    assert get_result(['A']) == 'You missed: A'
    assert get_result(['A', 'B', 'C']) == 'You missed: A, B, C'
