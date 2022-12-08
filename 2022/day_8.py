def day_8_input(filename):
    with open(filename) as f:
        return [[int(l) for l in [*line.strip()]] for line in f.readlines()]

def browse_direction(grid, direction):
    visible_trees = []
    match direction:
        case (0,1):
            for i, line in enumerate(grid):
                for j, _ in enumerate(line):
                    if (i == 0 or j == 0 or i == len(line)-1 or j == len(line)-1): continue
                    if not any(tree >= grid[i][j] for tree in line[:j]):
                        visible_trees.append((i,j))
        case (0,-1):
            for i, line in enumerate(grid):
                for j in range(len(line)-1, 0, -1):
                    if (i == 0 or j == 0 or i == len(line)-1 or j == len(line)-1): continue
                    if not any(tree >= grid[i][j] for tree in line[j+1:]):
                        visible_trees.append((i,j))
        case (1,0):
            for j in range(len(grid[0])):
                col = []
                for i in range(len(grid)):
                    if (i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1): continue
                    col.append(grid[i-1][j])
                    if not any(tree >= grid[i][j] for tree in col):
                        visible_trees.append((i,j))
        case (-1,0):
            for j in range(len(grid[0])):
                col = []
                for i in range(len(grid)-1,0,-1):
                    if (i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1): continue
                    col.append(grid[i+1][j])
                    if not any(tree >= grid[i][j] for tree in col):
                        visible_trees.append((i,j))
    return visible_trees

def browse_all_directions(grid):
    visible_trees = []
    directions = [((0,1)),(0,-1),(1,0),(-1,0)]
    for dir in directions:
        visible_trees += browse_direction(grid, dir)
    return list(set(visible_trees))

def find_out_scenic_score(grid, i, j):
    up = [grid[x][j] for x in range(0,i)][::-1]
    left = grid[i][:j][::-1]
    right = grid[i][j+1:]
    down = [grid[x][j] for x in range(i+1, len(grid))]
    directions = [up, left, right, down]
    
    scores = []
    for dir in directions:
        score = 0
        for elem in dir:
            if elem < grid[i][j]:
                score += 1
            else:
                score += 1
                break

        scores.append(score)

    return scores[0] * scores[1] * scores[2] * scores[3]


    
    #return up_score, left_score, right_score, down_score

def find_max_scenic_score(grid):
    max_scenic_score = 0
    for i, line in enumerate(grid):
        for j, _ in enumerate(line):
            score = find_out_scenic_score(grid, i, j)
            if score > max_scenic_score:
                max_scenic_score = score
    return max_scenic_score

grid = day_8_input('/home/romain/Documents/advent_of_code/2022/day_8_input.txt')
part1 = len(browse_all_directions(grid)) + len(grid)*4 - 4
print(part1)
part2 = find_max_scenic_score(grid)
print(part2)