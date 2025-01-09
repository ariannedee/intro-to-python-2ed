"""
Copilot response to the query:
 Write a function that, given a target word and a guessed word, returns a result like in Wordle,
 with one character to mark a letter in the correct place, another to mark a character in the wrong place,
 and another to mark incorrect characters.

 Can you give me some tests for it in pytest?
"""

import pytest


def wordle_feedback(target, guess):
    feedback = ['B'] * len(target)
    target_count = {}
    guess_count = {}

    # First pass: mark correct letters in the correct place
    for i in range(len(target)):
        if guess[i] == target[i]:
            feedback[i] = 'G'
        else:
            target_count[target[i]] = target_count.get(target[i], 0) + 1
            guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1

    # Second pass: mark correct letters in the wrong place
    for i in range(len(target)):
        if feedback[i] == 'B' and guess[i] in target_count and target_count[guess[i]] > 0:
            feedback[i] = 'Y'
            target_count[guess[i]] -= 1

    return ''.join(feedback)


def test_wordle_feedback():
    assert wordle_feedback("apple", "apric") == "GGYBB"
    assert wordle_feedback("apple", "apple") == "GGGGG"
    assert wordle_feedback("apple", "ppale") == "YGGYY"
    assert wordle_feedback("apple", "xxxxx") == "BBBBB"
    assert wordle_feedback("apple", "aplex") == "GGYBB"
    assert wordle_feedback("apple", "leapp") == "YYGGY"

if __name__ == "__main__":
    pytest.main()