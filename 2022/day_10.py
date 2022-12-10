def day_10_input(filename):
    instructions = open(filename).read().replace('addx', 'noop\naddx').split("\n")
    return instructions

instructions = day_10_input("/home/romain/Documents/advent_of_code/2022/day_10_input.txt")
register, p1, p2 = 1, 0, ""

for i, ins in enumerate(instructions):
    if i+1 in [20, 60, 100, 140, 180, 220]:
        p1 += (i+1)*register
    p2 += "#" if (i % 40) - 1 <= register <= (i % 40) + 1 else "."
    print(ins)
    if ins[0] == 'a':
        register += int(ins[4:])

print(p1)
for x in range(6):
    print(p2[40*x:40*x+40])

