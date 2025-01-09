"""
ChatGPT (Python) response to the query:
 Write a function that, given a target word and a guessed word, returns a result like in Wordle,
 with one character to mark a letter in the correct place, another to mark a character in the wrong place,
 and another to mark incorrect characters.

 Can you give me some tests for it in pytest?
"""

import pytest

# Sample implementation for reference (can be removed if testing only)
def wordle_feedback(target, guess):
    if len(target) != len(guess):
        raise ValueError("Target and guess words must be of the same length")

    feedback = ["⬛"] * len(target)  # Default to all incorrect
    target_chars = list(target)  # Convert to list for easier modification

    # Step 1: Mark all correct positions (🟩)
    for i, (t_char, g_char) in enumerate(zip(target, guess)):
        if g_char == t_char:
            feedback[i] = "🟩"
            target_chars[i] = None  # Mark this character as "used" in target_chars

    # Step 2: Mark misplaced characters (🟨)
    for i, g_char in enumerate(guess):
        if feedback[i] == "⬛" and g_char in target_chars:
            feedback[i] = "🟨"
            target_chars[target_chars.index(g_char)] = None  # Mark as used

    return feedback

# Test cases
def test_exact_match():
    assert wordle_feedback("apple", "apple") == ["🟩", "🟩", "🟩", "🟩", "🟩"]

def test_misplaced_characters():
    assert wordle_feedback("apple", "pleap") == ["🟨", "🟨", "🟨", "🟨", "🟨"]

def test_some_correct_some_incorrect():
    assert wordle_feedback("apple", "apply") == ["🟩", "🟩", "🟩", "🟨", "⬛"]

def test_all_incorrect():
    assert wordle_feedback("apple", "mango") == ["⬛", "⬛", "⬛", "⬛", "⬛"]

def test_repeating_characters_in_target():
    assert wordle_feedback("banana", "canada") == ["⬛", "🟩", "🟩", "⬛", "🟩", "⬛"]

def test_repeating_characters_in_guess():
    assert wordle_feedback("apple", "allee") == ["🟩", "⬛", "⬛", "🟨", "⬛"]

def test_mixed_correct_and_misplaced():
    assert wordle_feedback("table", "bleat") == ["🟨", "🟨", "🟨", "🟩", "🟨"]

def test_empty_string():
    assert wordle_feedback("", "") == []

def test_different_lengths():
    with pytest.raises(ValueError):
        wordle_feedback("apple", "app")

# Run pytest
if __name__ == "__main__":
    pytest.main()