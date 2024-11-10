def get_first(list: list[str]) -> str:
    """Return first element"""
    return list[0]


def remove_first(list: list[str]) -> None:
    """Remove first element"""
    list.pop(0)


def get_and_remove_first(list: list[str]) -> str:
    """Remove and return first element"""
    first: str = list[0]
    list.pop(0)
    return first
