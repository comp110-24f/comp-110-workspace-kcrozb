"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730755012"


def input_word() -> str:
    """User inputs a 5 letter word to be used for the game"""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return word


def input_letter() -> str:
    """User guesses a letter for the game"""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()
        return letter


def contains_char(word: str, letter: str) -> None:
    """Tests if the letter the user entered in found in the entered word.
    Prints what index the letter is found in or none if none.
    Also has a count variable that counts how many times letter is
    in word."""
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
