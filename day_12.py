from icecream import ic 
from collections import defaultdict, deque


def day_12_input(filename):
    caves = defaultdict(list)
    with open(filename) as file_input:
        values = file_input.readlines()
    for line in values:
        a, b = line.strip().split("-")
        caves[a].append(b)
        caves[b].append(a)
    return caves



def day_12_p1_p2():
    caves =day_12_input('day_12_input.txt')

    for skip_duplicates in True, False:
        count, search = 0, deque((child, set(), False) for child in caves["start"])

        while search:
            parent, lowers, duplicate = search.popleft()

            if parent == "end":
                count += 1
                continue
            elif parent.islower():
                if parent in lowers:
                    if skip_duplicates or duplicate:
                        continue
                    else:
                        duplicate = True
                lowers.add(parent)

            search.extend((child, set(lowers), duplicate) for child in caves[parent] if child != "start")

        ic(count)

day_12_p1_p2()