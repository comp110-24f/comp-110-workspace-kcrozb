"""Calculates my final grade for comp 110"""

__author__ = "730755012"


def ex_grade(input: list[float]) -> float:
    """Takes an input of a list of floats which are each individual
    ex grade and then returns a float which is the average of
    all the ex grades"""
    average: float = 0.0
    for value in input:
        average += value
    average = average / len(input)
    return average


def ls_grade(input: list[float]) -> float:
    """Takes an input of a list of floats which are each individual
    ls grade and then returns a float which is the average of
    all the ls grades"""
    average: float = 0.0
    for value in input:
        average += value
    average = average / len(input)
    return average


def cq_grade(input: list[float]) -> float:
    """Takes an input of a list of floats which are each individual
    cq grade and then returns a float which is the average of
    all the cq grades"""
    average: float = 0.0
    for value in input:
        average += value
    average = average / len(input)
    return average


def quiz_grade(input: list[float]) -> float:
    """Takes an input of a list of floats which are each individual
    quiz grade and then returns a float which is the average of
    all the quiz grades"""
    average: float = 0.0
    for value in input:
        average += value
    average = average / len(input)
    return average


def total_grade(ex: float, ls: float, cq: float, quiz: float, exam: float) -> float:
    return (
        (ex * (3 / 10))
        + (ls * (1 / 10))
        + (cq * (1 / 10))
        + (quiz * (4 / 10))
        + (quiz * (1 / 10))
        + (exam * (1 / 10))
    )


exg: list[float] = [85.0, 80.0, 70.0, 75.5]
"""latest grade was wordle"""
lsg: list[float] = [
    100.0,
    100.0,
    100.0,
    100.0,
    100.0,
    100.0,
    80.0,
    87.5,
    100.0,
    100.0,
    100.0,
    100.0,
    88.8,
    92.3,
    83.3,
    100.0,
    100.0,
    100.0,
    100.0,
]
"""latest grade was ls18"""
cqg: list[float] = [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
"""latest grade was cq05"""
quizg: list[float] = [98.4, 88.1, 86.36]
"""latest was qz02"""
print(
    total_grade(
        ex=ex_grade(exg),
        ls=ls_grade(lsg),
        cq=cq_grade(cqg),
        quiz=quiz_grade(quizg),
        exam=80.0,
    )
)
