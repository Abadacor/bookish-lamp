from icecream import ic 

def day_13_input(filename):
    with open(filename) as file:
        marks, folds = file.read().split("\n\n")
        marks = {(int(x), int(y)) for x, y in (row.split(",") for row in marks.splitlines())}
        folds = [(axis, int(pos)) for axis, pos in (row.split(" ")[-1].split("=") for row in folds.splitlines())]
    return marks, folds

def fold(x, y, axis, pos):
    if axis == "x":
        if x == pos:
            return None
        return (x, y) if x < pos else ((2 * pos - x), y)
    else:
        if y == pos:
            return None
        return (x, y) if y < pos else (x, 2 * pos - y)

def day_13_p1():
    marks, folds = day_13_input('day_13_input.txt')
    after_fold = []
    for x, y in marks:
        if (fold(x, y, folds[0][0], folds[0][1])):
            after_fold.append(fold(x, y, folds[0][0], folds[0][1]))
    return len(set(after_fold))

def day_13_p2():
    marks, folds = day_13_input('day_13_input.txt')
    for i in range(len(folds)):
        # I could replace the whole contents of this loop by this line:
        # marks = {dot for x, y in marks if (dot:=fold(x, y, folds[i][0], folds[i][1]))}
        # But, until i'm capable of thinking of it on my own, I won't
        # also people on SO are fucking mad.
        folded = []
        for x, y in marks:
            if (fold(x, y, folds[i][0], folds[i][1])):
                folded.append(fold(x, y, folds[i][0], folds[i][1]))
        folded = set(folded)
        marks = folded
    
    width = max(x for x, y in marks) + 1
    height = max(y for x, y in marks) + 1
    grid = [[" " for _ in range(width)] for _ in range(height)]
    for x, y in marks:
        grid[y][x] = "#"
    for row in grid:
        print("".join(row))
        
ic(day_13_p1())
day_13_p2()