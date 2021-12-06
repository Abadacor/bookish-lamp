import numpy as np
from icecream import ic


def day_5_input(filename):
    with open(filename) as file_input:
        vectors = file_input.readlines()
    for i, _ in enumerate(vectors):
        vectors[i] = vectors[i].split("->")
        for j, _ in enumerate(vectors[i]):
            vectors[i][j] = vectors[i][j].split(",")
            for k, _ in enumerate(vectors[i][j]):
                vectors[i][j][k] = int(vectors[i][j][k])
    return vectors


def filter_input_for_p1(clean_vectors):
    samesies = []
    for elem in clean_vectors:
        if (elem[0][0] == elem[1][0]) or (elem[0][1] == elem[1][1]):
            samesies.append(elem)
    return samesies


def define_elem(elem):
    if elem[0][0] == elem[1][0]:
        row = True
        same = elem[0][0]
        if elem[0][1] >= elem[1][1]:
            start = elem[0][1]
            end = elem[1][1]
        else:
            end = elem[0][1]
            start = elem[1][1]
    elif elem[0][1] == elem[1][1]:
        row = False
        same = elem[0][1]
        if elem[0][0] >= elem[1][0]:
            start = elem[0][0]
            end = elem[1][0]
        else:
            end = elem[0][0]
            start = elem[1][0]
    return same, end, start, row


def define_elem_p2(elem):
    return True


def day_5_p1():
    values = filter_input_for_p1(day_5_input("day_5_input.txt"))
    grid = np.zeros([1000, 1000])

    for elem in values:
        same, start, end, row = define_elem(elem)
        for i in range(start, end + 1):
            if row:
                grid[same][i] += 1
            else:
                grid[i][same] += 1

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] >= 2:
                count += 1

    return count


def day_5_p2():
    values = day_5_input("day_5_input.txt")
    grid = np.zeros([1000, 1000])

    for elem in values:
        if (elem[0][0] == elem[1][0]) or (elem[0][1] == elem[1][1]):
            same, start, end, row = define_elem(elem)
            for i in range(start, end + 1):
                if row:
                    grid[same][i] += 1
                else:
                    grid[i][same] += 1
        else:
            start_x = elem[0][0]
            start_y = elem[0][1]
            end_x = elem[1][0]
            end_y = elem[1][1]

            x = start_x
            y = start_y

            if start_x >= end_x:
                if start_y <= end_y:
                    while x >= end_x and y <= end_y:
                        grid[x][y] += 1
                        x -= 1
                        y += 1
                else:
                    while x >= end_x and y >= end_y:
                        grid[x][y] += 1
                        x -= 1
                        y -= 1
            else:
                if start_y <= end_y:
                    while x <= end_x and y <= end_y:
                        grid[x][y] += 1
                        x += 1
                        y += 1
                else:
                    while x <= end_x and y >= end_y:
                        grid[x][y] += 1
                        x += 1
                        y -= 1

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] >= 2:
                count += 1

    return count


ic(day_5_p2())
