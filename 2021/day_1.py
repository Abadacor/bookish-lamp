"""
This module presents the solution for day 1 of the advent of code challenge
"""


def day_1(filename):
    """
    This function takes a file containing values separated by a \\n and according to a window size of 3 returns the sum of time the window was greater than the previous one.
    """
    with open(filename) as sonar_file:
        depth_measures = sonar_file.readlines()

    depth_measures = depth_measures[:-1]
    for i, _ in enumerate(depth_measures):
        depth_measures[i] = int(depth_measures[i][:-1])

    sums = []
    i = 0
    while i <= (len(depth_measures) - 3):
        sums.append(depth_measures[i] + depth_measures[i + 1] + depth_measures[i + 2])
        i += 1

    inc = 0
    equal = 0
    dec = 0

    for i, _ in enumerate(sums):
        if i == 0:
            continue
        if sums[i - 1] < sums[i]:
            inc += 1
        elif sums[i - 1] == sums[i]:
            equal += 1
        else:
            dec += 1

    return [inc, equal, dec]


print(day_1("day_1_input.txt"))
