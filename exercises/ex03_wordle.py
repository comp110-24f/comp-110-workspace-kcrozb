"""Wordle Assignment"""

__author__ = "730755012"


def input_guess(length: int) -> str:
    """User inputs a guess that needs to be the same length as the
    secret word"""
    guess = input("Enter a " + str(length) + " character word: ")
    while len(guess) != length:
        guess = input("That wasn't 5 chars! Try again: ")
    return guess


def contains_char(word: str, letter: str) -> bool:
    """tests the index's of the first parameter to see if they
    match with the second one. returns true if there is a match
    and returns false otherwise"""
    assert len(letter) == 1
    index: int = 0
    while index < len(word):
        if word[index] == letter:
            return True
        index = index + 1
    else:
        return False


def emojified(guess: str, secret_word: str) -> str:
    """Visually represents the accuracy of a guess in relation to
    a secret word using emojis"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    return_value: str = ""
    idx: int = 0
    while idx < len(secret_word):
        if guess[idx] == secret_word[idx]:
            return_value = return_value + GREEN_BOX
            idx = idx + 1
        elif contains_char(secret_word, guess[idx]) is True:
            return_value = return_value + YELLOW_BOX
            idx = idx + 1
        else:
            return_value = return_value + WHITE_BOX
            idx = idx + 1
    return return_value


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    number_of_turns: int = 1
    turns_limit: int = 6
    while number_of_turns <= turns_limit:
        print("=== Turn " + str(number_of_turns) + "/" + str(turns_limit) + " ===")
        guess = input_guess(len(secret))
        print(emojified(guess=guess, secret_word=secret))
        if guess == secret:
            print(
                "You won in "
                + str(number_of_turns)
                + "/"
                + str(turns_limit)
                + " turns!"
            )
            number_of_turns = 7
        elif number_of_turns == 6:
            print("X/" + str(turns_limit) + " - Sorry, try again tomorrow!")
        number_of_turns += 1


if __name__ == "__main__":
    main(secret="codes")
