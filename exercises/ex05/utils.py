"""File for ex05"""

__author__ = "730755012"


def only_evens(input: list[int]) -> list[int]:
    """returns a new list of only even elements in the original list"""
    even_list: list[int] = list()
    for number in input:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """generates a list that is a subset of the input list. sub
    starts at the start index and ends at the end index - 1"""
    if start < 0:
        start = 0
    if end > len(input):
        end = len(input) - 1
    sub_list: list[int] = list()
    if len(input) == 0:
        return sub_list
    if start >= len(input):
        return sub_list
    if end <= 0:
        return sub_list
    for number in range(start, end):
        sub_list.append(input[number])
    return sub_list


def add_at_index(input: list[int], add: int, index: int) -> None:
    """mutates input list by adding element at given index"""
    if (index < 0) or (index > len(input)):
        raise IndexError("Index is out of bounds for the input list")
    else:
        second_half: list[int] = []
        idx: int = index
        while idx < len(input):
            second_half.append(input[idx])
            idx += 1
        ind: int = len(input) - 1
        while ind >= index:
            input.pop(ind)
            ind = ind - 1
        input.append(add)
        input.extend(second_half)


"""numbers: list[int] = [1, 2, 3, 4, 5, 6]
add_at_index(input=numbers, add=12, index=3)
print(numbers)"""
