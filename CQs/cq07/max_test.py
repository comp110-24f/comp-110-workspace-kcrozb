__author__ = "730755012"
from CQs.cq07.find_max import find_and_remove_max


def test_return_value() -> None:
    """Tests for the expected return value of find and remove max"""
    numbers: list[int] = [1, 2, 3, 4, 4, 3, 2, 4]
    assert find_and_remove_max(input=numbers) == 4


def test_mutate() -> None:
    """Tests to make sure the input is correctly mutated"""
    numbers: list[int] = [1, 2, 3, 4, 4, 3, 2, 4]
    find_and_remove_max(input=numbers)
    assert numbers == [1, 2, 3, 3, 2]


def test_edge_case() -> None:
    """Tests the edge case in case of an unconventional input"""
    numbers: list[int] = []
    assert find_and_remove_max(numbers) == -1
