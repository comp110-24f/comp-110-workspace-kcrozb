from Lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    fruits: list[str] = ["apples", "oranges", "bannanas"]
    assert get_first(fruits) == "apples"


def test_remove_first_ret_value() -> None:
    """test that remove first returns none"""
    fruits: list[str] = ["apples", "oranges", "bannanas"]
    assert remove_first(fruits) is None


def test_remove_first_behavior() -> None:
    fruits: list[str] = ["apples", "oranges", "bannanas"]
    remove_first(fruits)
    assert fruits == ["oranges", "bannanas"]


def test_get_and_remove_first() -> None:
    fruits: list[str] = ["apples", "oranges", "bannanas"]
    assert get_and_remove_first(fruits) == "apples"
