"""
This module presents the solution for day 3 of the advent of code challenge.
"""
import numpy as np


def split(word):
    """
    You can see what this does.
    """
    return [int(char) for char in word]


def day_3_input(filename):
    """
    This gives the input matrix for the challenge using numpy
    """
    with open(filename) as input_file:
        report = input_file.readlines()

    for i, _ in enumerate(report):
        report[i] = np.array(split(report[i][:-1]))

    return np.array(report)


def day_3_p1():
    """
    This function takes a matrix of binary numbers as input and sums the most and less common bits for each column and returns the product in decimal of those two numbers.
    """
    report = day_3_input("day_3_input.txt")
    return (lambda x: x * (~x & (2 ** 12 - 1)))(
        int(
            "".join(
                [
                    ("1" if value >= len(report) / 2 else "0")
                    for value in np.sum(report, axis=0)
                ]
            ),
            2,
        )
    )


def day_3_p2():
    """
    This function gets the oxygen generator rating and co2 scrubber rating and returns their product.
    """
    report = day_3_input("day_3_input.txt")
    gen_rating_indexes = list(range(1000))
    scrubber_indexes = list(range(1000))

    for i in range(len(report[0])):
        bit_criteria_gen = (1 if np.sum(report[gen_rating_indexes], axis=0)[i] >= len(gen_rating_indexes)/2 else 0)
        bit_criteria_scrub = (1 if np.sum(report[scrubber_indexes], axis=0)[i] >= len(scrubber_indexes)/2 else 0)

        for j, item in enumerate(report):
            if item[i] != bit_criteria_gen and len(gen_rating_indexes) > 1 and j in gen_rating_indexes:
                gen_rating_indexes.remove(j)
            if item[i] == bit_criteria_scrub and len(scrubber_indexes) > 1 and j in scrubber_indexes:
                scrubber_indexes.remove(j)

    generator_rating = "".join([str(bit) for bit in report[gen_rating_indexes[0]].tolist()])
    scrubber_rating = "".join([str(bit) for bit in report[scrubber_indexes[0]].tolist()])

    return int(generator_rating, 2) * int(scrubber_rating, 2)


print(day_3_p2())
