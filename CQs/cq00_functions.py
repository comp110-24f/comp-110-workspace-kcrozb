_author_ = "730755012"


def mimic(message: str) -> str:
    """Mimics a message"""
    return message


def main() -> None:
    """Print the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
