from itertools import accumulate


def day_7_input(filename):
    with open(filename) as f:
        printout = f.readlines()
        printout = [command.strip() for command in printout]
    return printout

def find_sizes(printout):
    s = []
    R = []
    for line in printout:
        command = line.split(" ")
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "..":
                    R.append(s.pop())
                    s[-1] += R[-1]
                else:
                    s.append(0)
        elif command[0] != "dir":
            s[-1] += int(command[0])
    """
    okay you're gonna forget this so:
    R contains all directories you've finished browsing and for whom you know the final size
    S contains all the directories that might change size with the rest of instructions
    so when you finish all instructions s contains the last "branch" of directories and their local sizes.
    So for each elem of s (starting with the last one cuz it's the last nested dir), you need to add to it the size of the directories it contains and then add it to R
    accumulate() does that, it gives you the total sum at the point you are in the iteration.
    accumulate([1,2,3,4]) = [1,3,6,10]
    except it returns a fucking iterator, so you cast it as a list.
    got it? no? thought so. well enjoy the next 30min.
    """
    return R + list(accumulate(reversed(s)))

def part1(printout):
    return sum([x for x in find_sizes(printout) if x<=100000])

def part2(printout):
    R = find_sizes(printout)
    available = 70000000-R[-1]
    return min([x for x in R if x+available>=30000000])

printout = day_7_input('/home/romain/Documents/advent_of_code/2022/day_7_input.txt')
print(part1(printout))
print(part2(printout))