import sys

DELTA = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def day_9_input(filename):
    with open(filename) as f:
        instructions = [inst.strip() for inst in f.readlines()]
        instructions = [(a, int(b)) for a, b in [line.split(" ") for line in instructions]]
    return instructions

def set_pos(pos):
    for i in range(len(pos)-2, -1, -1):
        x, y = pos[i+1]
        dx, dy = pos[i]
        if abs(x-dx) > 1 or abs(y-dy) > 1:
            if x > dx:
                dx += 1
            elif x < dx:
                dx -= 1
            if y > dy:
                dy += 1
            elif y < dy:
                dy -= 1
            pos[i] = (dx, dy)

instructions = day_9_input('/home/romain/Documents/advent_of_code/2022/day_9_input.txt')

tailpt1, tailpt2 = set(), set()
x = y = 0
pos = [(0,0)] * 10
for (a, b) in instructions:
    c = DELTA[a]
    for i in range(b):
        x += c[0]
        y += c[1]
        pos[-1] = (x, y)
        set_pos(pos)
        tailpt1.add(pos[-2])
        tailpt2.add(pos[0])

print(len(tailpt1), len(tailpt2))