"""Mutating functions"""

__author__ = "730755012"


def manual_append(listy: list[int], number: int) -> None:
    listy.append(number)


def double(lister: list[int]) -> None:
    idx: int = 0
    while idx < len(lister):
        lister[idx] = lister[idx] * 2
        idx = idx + 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
