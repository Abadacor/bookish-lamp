import enum
from icecream import ic
import numpy as np

def day_9_input(filename):
    with open(filename) as file_input:
        heights = file_input.readlines()
    for i, line in enumerate(heights):
        line = line.strip()
        heights[i] = np.array([int(line[i : i + 1]) for i in range(0, len(line))])
    heights = np.array(heights)
    return heights

def neighbours(y, x):
    neighs = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    return [(a, b) for a, b in neighs if 0 <= a < 100 and 0 <= b < 100]

def day_9_p1():
    heights = day_9_input("day_9_input.txt")
    lowpoints = []
    for y, _ in enumerate(heights):
        for x, _ in enumerate(heights[0]):
            if all(heights[y][x] < heights[a][b] for a, b in neighbours(y, x)):
                lowpoints.append((y, x))

    return lowpoints, sum(heights[y][x] + 1 for y, x in lowpoints)

def get_basin(heights,y, x):
    basin = {(y, x)}
    for a, b in neighbours(y, x):
        if heights[y][x] < heights[a][b] < 9:
            basin |= get_basin(heights, a, b)
    return basin

def day_9_p2():
    heights = day_9_input("day_9_input.txt")
    lowpoints, _ = day_9_p1()
    basin_sizes = sorted([len(get_basin(heights, y, x)) for y, x in lowpoints])
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
    
ic(day_9_p1())
ic(day_9_p2())
