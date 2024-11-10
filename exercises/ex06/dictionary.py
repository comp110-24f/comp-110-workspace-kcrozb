"""ex06 Assignment"""

__author__ = """730755012"""


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Switches the values with the keys in a new dictionary.
    Cannot have same two values in input_dict because this will
    raise a key error when you try to invert them"""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate value found")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(favorites: dict[str, str]) -> str:
    """Takes a dictionary of peoples names and favorite colors.
    It returns the most popular favorite color. In the case of
    a tie it returns the first color in the tie"""
    color_count = {}
    first_occurrence = {}
    for name, color in favorites.items():
        if color not in color_count:
            color_count[color] = 0
            first_occurrence[color] = name
        color_count[color] += 1
    most_popular_color: str = ""
    max_count = 0
    for color, count in color_count.items():
        if count > max_count or (
            count == max_count
            and first_occurrence[color] < first_occurrence[most_popular_color]
        ):
            most_popular_color = color
            max_count = count
    return most_popular_color


def count(input_list: list[str]) -> dict[str, int]:
    """Takes each string in a list and uses it to create a key
    in a dictionary. The value associated with the key is
    equal to the number of times the key is in the input list"""
    result: dict[str, int] = dict()
    for value in input_list:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Takes words from an input list and groups them based on the
    letter that they start with. The key in the dictionary
    is the first letter. The values are the words which are
    stored in a list. Uppercase and lowercase of the same letter are
    grouped together"""
    alphabet: dict[str, list[str]] = {}
    for word in input:
        first_letter: str = word[0].lower()
        if first_letter not in alphabet:
            alphabet[first_letter] = []
        alphabet[first_letter].append(word)
    return alphabet


def update_attendance(attendance: dict[str, list[str]], day: str, name: str) -> None:
    """Function that updates the attendance for a given day of the week.
    The key is the day and the value is the list of names of students
    present on that day of the week."""
    if day not in attendance:
        attendance[day] = []
    attendance[day].append(name)
