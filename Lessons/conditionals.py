"""Practicing my Conditionals"""


def less_than_10(num: int) -> bool:
    """Tell us if num < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        return True  # "then" block
    else:
        return False


print(less_than_10(num=11))


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off"""
    if alarm is True:
        return "Wake up! Go to comp 110"
    else:
        return "Keep sleeping. You deserve it"


print(wake_up(alarm=False))


def check_first_letter(word: str, letter: str) -> None:
    if word[0] == letter:
        print("match!")
    else:
        print("no match")


check_first_letter("happy", "h")
check_first_letter("griddy", "l")
