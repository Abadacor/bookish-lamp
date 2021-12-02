"""
This module presents the solution for day 2 of the advent of code challenge.
"""


def day_2(filename):
    """
    This function figures out the product of the positions of a submarine according to the data input given in parameter.
    """

    with open(filename) as input_file:
        directions = input_file.readlines()

    for i, _ in enumerate(directions):
        directions[i] = directions[i][:-1].split(" ")
        directions[i][1] = int(directions[i][1])

    aim = 0
    horizontal_position = 0
    depth = 0

    for item in directions:
        if item[0] == "forward":
            horizontal_position += item[1]
            depth += aim * item[1]
        elif item[0] == "up":
            aim -= item[1]
        elif item[0] == "down":
            aim += item[1]
        else:
            continue

    return horizontal_position * depth


print(day_2("day_2_input.txt"))
