
from icecream import ic 
from re import findall
from math import sqrt

def day_17_input(filename):
    with open(filename) as file_input:
        ints = [int(i) for i in findall(r'-?\d+', file_input.read().strip())]
    return ints

def reaches_target(v, t_min, t_max):
    p = [0, 0]
    while True:
        for i in range(2): p[i] += v[i]
        v[0] -= 1 if v[0] else 0
        v[1] -= 1
        if p[0] > t_max[0] or p[1] < t_min[1]: return False
        if all((t_min[i] <= p[i] <= t_max[i] for i in range(2))): return True

def day_17_p1():
    ints = day_17_input('day_17_input.txt')
    t_min = (ints[0], ints[2]) # 150, -129
    t_max = (ints[1], ints[3]) # 171, -70
    v0_min = (int(sqrt(t_min[0] * 2)), t_min[1])
    v0_max = (t_max[0], abs(t_min[1] + 1))
    ic(int(sqrt(t_min[0] * 2)), int(sqrt()))
    ic((v0_max[1] + 1) * v0_max[1] // 2)
    ic(v0_max[1]) + sum([i for i in range(v0_max[1])])

    return t_min, t_max, v0_min, v0_max

def day_17_p2():
    t_min, t_max, v0_min, v0_max = day_17_p1()
    r2 = 0
    for v0_x in range(v0_min[0], v0_max[0] + 1):
        for v0_y in range(v0_min[1], v0_max[1] + 1):
            r2 += reaches_target([v0_x, v0_y], t_min, t_max)

    ic(r2)

day_17_p2()