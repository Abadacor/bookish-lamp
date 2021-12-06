from icecream import ic
from functools import reduce

def day_6_input(filename):
    with open(filename) as file_input:
        values = [int(val) for val in file_input.readline().split(',')]
    
    return values

def day_6_p1():
    values = day_6_input('day_6_input.txt')

    for i in range(80):
        new_fish = 0
        for j, fish in enumerate(values):
            if(fish == 0):
                values[j] = 6
                new_fish += 1
            else:
                values[j] -= 1
        for j in range(new_fish):
            values.append(8)

    return len(values)

def day_6_p2():
    values = day_6_input('day_6_input.txt')
    populations = [0 for _ in range(9)]
    for i in range(7):
        populations[i] = values.count(i)
    populations[8] = 0

    for i in range(256):
        new_fish = populations[0]
        populations.pop(0)
        populations[6] += new_fish
        populations.append(new_fish)

    return reduce(lambda x, y: x+y, populations)

ic(day_6_p2())