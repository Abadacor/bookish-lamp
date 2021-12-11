from icecream import ic 
import numpy as np

def day_11_input(filename):
    with open(filename) as file_input:
        return np.array([np.array([int(val.strip()[i : i + 1]) for i in range(0, len(val.strip()))]) for val in file_input.readlines()])

def neighbours(i, j):
    neighs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j+1)]
    return [(a, b) for a, b in neighs if 0 <= a < 10 and 0 <= b < 10]

def increase_adjacent(matrix, i, j):
    for (a, b) in neighbours(i, j):
        if matrix[a][b] > 0:
            matrix[a][b] += 1 
    return matrix

def process_first_flash_found(matrix):
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[0]):
            if matrix[i][j] > 9:
                matrix = increase_adjacent(matrix,i,j)
                matrix[i][j] = 0
                return False, matrix
    return True, matrix

def process_all_flashes(matrix, flashes):
    darkness = False
    while not darkness:
        darkness, matrix = process_first_flash_found(matrix)
        flashes += 1
    # -1 because when there are no flashes to process, there still is one increment
    return matrix, flashes-1

def step(matrix, flashes):
    matrix += 1
    return process_all_flashes(matrix, flashes)

def izall_flashing(matrix):
    return np.all((matrix == 0))

def day_11_p1():
    values = day_11_input('day_11_input.txt')
    flashes = 0
    for i in range(100):
        values, flashes = step(values, flashes)
    return values, flashes

def day_11_p2():
    count = 0
    flashes = 0
    values = day_11_input('day_11_input.txt')
    while not izall_flashing(values):
        values, flashes = step(values, flashes)
        count += 1
    return count

ic(day_11_p1())
ic(day_11_p2())