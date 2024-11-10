"""Basic syntax of lists"""

names: list[str] = list()  # empty list w/ constructor
my_numbers: list[float] = []  # empty list w/ literal

names.append("Kacey")  # add an item to a list
my_numbers.append(1.5)  # appending example

print(my_numbers)

game_points: list[int] = [102, 86, 94]  # create a list with values
print(game_points[2])  # subscription notation/indexing

game_points[1] = 72  # modify a list
print(game_points)

print(len(game_points))  # print the length of a list

game_points.pop(1)  # removes an item from a list
print(game_points)

# write a function called display
# Input: list[int]
# Return Value: None
# Loop over the input and print every value
# Try calling it on game_points!


def looper(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index = index + 1


looper(input=game_points)
