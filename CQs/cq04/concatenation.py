__author__ = """730755012"""


def concat(string1: str, string2: str) -> str:
    combine: str = string1 + string2
    return combine


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
