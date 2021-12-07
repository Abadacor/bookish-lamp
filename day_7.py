from icecream import ic
import numpy as np
import math

def day_7_input(filename):
    with open(filename) as file_input:
        positions = [int(pos) for pos in file_input.readline().split(',')]
    return positions

def day_7_p1():
    positions = np.array(day_7_input('day_7_input.txt'))
    median = round(np.median(positions))
    fuel = 0

    for pos in positions:
        fuel += (median - pos) if(pos < median) else(pos - median)

    return fuel

def day_7_p2():
    positions = day_7_input('day_7_input.txt')
    fuel = float("inf")

    for pos in range(min(positions), max(positions) + 1):
        diffs = [abs(pos - i) for i in positions]
        sums = [(n*(n+1))/2 for n in diffs]
        fuel = min(fuel, sum(sums))
    return round(fuel)

ic(day_7_p1())
ic(day_7_p2())