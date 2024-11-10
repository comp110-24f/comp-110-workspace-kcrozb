__author__ = "730755012"


def find_and_remove_max(input: list[int]) -> int:
    """Finds the largest value in the input list, removes all
    instances of this value from the list, and then returns the
    max value"""
    if len(input) == 0:
        return -1
    max: int = input[0]
    for instance in input:
        if instance > max:
            max = instance
    index: int = 0
    while index < len(input):
        if input[index] == max:
            input.pop(index)
        else:
            index = index + 1
    return max
