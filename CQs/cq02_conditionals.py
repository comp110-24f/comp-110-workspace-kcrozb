"""Practice with conditionals, local variables, and user input"""

__author__ = "730755012"


def guess_a_number() -> None:
    secret: int = 7
    x: str = input("Guess a number:")
    print("Your guess was " + x)
    if secret == int(x):
        print("You got it!")
    elif secret > int(x):
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
