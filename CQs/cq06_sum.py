"""Summing the elements of  a list using different loops"""

__author__ = "730755012"

vals: list[float] = [1, 2, 3, 4]


def w_sum(vals: list[float]) -> float:
    sum: float = 0
    index: int = 0
    if len(vals) == 0:
        return 0.0
    while index < len(vals):
        sum = sum + vals[index]
        index = index + 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0
    if len(vals) == 0:
        return 0.0
    for number in vals:
        sum += number
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0
    if len(vals) == 0:
        return 0.0
    for number in range(len(vals)):
        sum = sum + vals[number]
    return sum
