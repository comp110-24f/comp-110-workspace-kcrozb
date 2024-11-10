"""assignment"""

__author__ = "730755012"


def all(list: list[int], number: int) -> bool:
    index: int = 0
    count: int = 0
    while index < len(list):
        if list[index] != number:
            count = count + 1
        index = index + 1
    if len(list) == 0:
        return False
    elif count > 0:
        return False
    else:
        return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 1
    max_value: int = input[0]
    while idx < len(input):
        if input[idx] > max_value:
            max_value = input[idx]
        idx = idx + 1
    return max_value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    if len(list_1) != len(list_2):
        return False
    idx: int = 0
    count: int = 0
    while idx < len(list_1):
        if list_1[idx] != list_2[idx]:
            count = count + 1
        idx = idx + 1
    if count > 0:
        return False
    else:
        return True


def extend(a: list[int], b: list[int]) -> None:
    idx: int = 0
    while idx < len(b):
        a.append(b[idx])
        idx = idx + 1
