"""
ChatGPT response to the query:
 Write a function that, given a target word and a guessed word, returns a result like in Wordle,
 with one character to mark a letter in the correct place, another to mark a character in the wrong place,
 and another to mark incorrect characters.

 Can you give me some tests for it in pytest?
"""
import pytest


def wordle_feedback(target, guess):
    # Initialize result with all "⬛" for each letter in the guess
    result = ["⬛"] * len(guess)
    target_chars = list(target)

    # Step 1: Check for correct letters in correct positions (green)
    for i, (g, t) in enumerate(zip(guess, target)):
        if g == t:
            result[i] = "🟩"
            target_chars[i] = None  # Mark this letter as matched

    # Step 2: Check for correct letters in wrong positions (yellow)
    for i, g in enumerate(guess):
        if result[i] == "⬛" and g in target_chars:
            result[i] = "🟨"
            target_chars[target_chars.index(g)] = None  # Remove matched letter from target_chars

    return "".join(result)


def test_all_correct():
    assert wordle_feedback("apple", "apple") == "🟩🟩🟩🟩🟩", "All letters and positions are correct"

def test_some_correct_positions():
    assert wordle_feedback("apple", "apart") == "🟩🟩⬛⬛⬛", "Only the first two letters are correct and in the right position"

def test_some_wrong_positions():
    assert wordle_feedback("apple", "pearl") == "🟨🟨🟩⬛⬛", "Letters p, e are correct but in the wrong position; a is in the right position"

def test_all_incorrect():
    assert wordle_feedback("apple", "xxxxx") == "⬛⬛⬛⬛⬛", "None of the guessed letters are correct"

def test_mixed_positions():
    assert wordle_feedback("table", "bleat") == "🟨🟨🟨🟨🟨", "All letters are correct but in the wrong position"

def test_partial_correct_mixed_positions():
    assert wordle_feedback("apple", "plead") == "🟨🟩🟨⬛⬛", "p, l, e are correct but in mixed positions"

def test_duplicates_in_target():
    assert wordle_feedback("apple", "apply") == "🟩🟩🟩🟩⬛", "All letters match except the last one, 'y'"

def test_duplicates_in_guess():
    assert wordle_feedback("apple", "ppppp") == "⬛🟩🟩⬛⬛", "Only the middle letters 'p' match correctly"

def test_partial_match_with_duplicates():
    assert wordle_feedback("banana", "canada") == "⬛🟨🟩🟨⬛⬛", "Correct letters 'a' and 'n' are mixed with some correct positions"

if __name__ == "__main__":
    pytest.main()
