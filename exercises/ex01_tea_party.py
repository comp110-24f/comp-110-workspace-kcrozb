"""Calculates the total number or tea bags, treats, and cost
to host a tea party based on number of guests"""

__author__: str = "730755012"


def main_planner(guests: int) -> None:
    """Brings all other functions together to produce an output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Computes the number of tea bags based on the number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Determines the number of treats needed based on number on people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost based on how many tea bags and treats"""
    return float(tea_count * 0.50 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending?")))
