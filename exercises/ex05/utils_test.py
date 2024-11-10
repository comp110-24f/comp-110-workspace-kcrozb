"""File for ex05"""

__author__ = "730755012"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_return_value() -> None:
    """Tests that the return value of only_evens is correct"""
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(numbers) == [2, 4, 6]


def test_only_evens_no_mutate() -> None:
    """Tests that only_evens does not mutate the input list"""
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    only_evens(numbers)
    assert numbers == [1, 2, 3, 4, 5, 6]


def test_only_evens_odds() -> None:
    """Input list of only odd numbers should return an empty list"""
    numbers: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(numbers) == []


def test_sub_return_value() -> None:
    """Tests that the return value of sub is correct"""
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(numbers, 1, 4) == [2, 3, 4]


def test_sub_no_mutate() -> None:
    """tests that the sub function does not mutate input list"""
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    sub(numbers, 1, 4)
    assert numbers == [1, 2, 3, 4, 5, 6]


def test_sub_edge_case_start() -> None:
    """Tests that sub returns an empty list when start is greater
    than the length of the list"""
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(numbers, 9, 10) == []


def test_add_at_index_return() -> None:
    """Tests to make sure that the function returns nothing"""
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    assert add_at_index(numbers, 2, 5) is None


def test_add_at_index_modify() -> None:
    """Tests that the input list has been correctly modified"""
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    add_at_index(numbers, 10, 2)
    assert numbers == [1, 2, 10, 3, 4, 5, 6]


def test_add_at_index_raises_indexerror() -> None:
    """Makes sure error is raised when an out of range index is
    given"""
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    with pytest.raises(IndexError):
        add_at_index(numbers, 10, 70)
