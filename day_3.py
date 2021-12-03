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
    sums = np.sum(report, axis=0)
    gamma_rate = ""
    epsilon_rate = ""
    for value in sums:
        if value >= len(report) / 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def day_3_p2():
    """
    This function gets the oxygen generator rating and co2 scrubber rating and returns their product.
    """
    report = day_3_input("day_3_input.txt")
    gen_rating_indexes = list(range(1000))
    scrubber_indexes = list(range(1000))
    for i in range(len(report[0])):
        bit_criteria_gen = np.sum(report[gen_rating_indexes], axis=0)[i]
        if bit_criteria_gen >= len(gen_rating_indexes) / 2:
            bit_criteria_gen = 1
        else:
            bit_criteria_gen = 0
        bit_criteria_scrub = np.sum(report[scrubber_indexes], axis=0)[i]
        if bit_criteria_scrub >= len(scrubber_indexes) / 2:
            bit_criteria_scrub = 1
        else:
            bit_criteria_scrub = 0

        for j, item in enumerate(report):
            if item[i] != bit_criteria_gen and len(gen_rating_indexes) > 1:
                if j in gen_rating_indexes:
                    gen_rating_indexes.remove(j)
            if item[i] == bit_criteria_scrub and len(scrubber_indexes) > 1:
                if j in scrubber_indexes:
                    scrubber_indexes.remove(j)
        print(len(gen_rating_indexes), len(scrubber_indexes))

    generator_rating = report[gen_rating_indexes[0]].tolist()
    generator_rating = [str(bit) for bit in generator_rating]
    generator_rating = "".join(generator_rating)

    scrubber_rating = report[scrubber_indexes[0]].tolist()
    scrubber_rating = [str(bit) for bit in scrubber_rating]
    scrubber_rating = "".join(scrubber_rating)
    print(generator_rating, scrubber_rating)
    return int(generator_rating, 2) * int(scrubber_rating, 2)


print(day_3_p2())
