"""While loops practice"""

__author__ = "730755012"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
            index = index + 1
        else:
            index = index + 1
    return count
