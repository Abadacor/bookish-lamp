from icecream import ic 
import numpy as np
from queue import PriorityQueue
from collections import defaultdict

def day_15_input(filename):
    with open(filename) as file_input:
        grid = file_input.read()
        grid = [[int(i) for i in line] for line in grid.splitlines()]
    return grid

def shortest(grid, start):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    end = len(grid) - 1, len(grid) - 1
    n = len(grid)
    
    q = PriorityQueue()
    q.put((0, start))
    
    dists = defaultdict(lambda :float('inf'))
    dists[start] = 0
    
    while not q.empty():
        d, node = q.get()
        if node == end: return d
        if dists[node] < d: continue
        
        i, j = node
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni in (-1, n) or nj in (-1, n): continue
            new_d = d + grid[ni][nj]
            if dists[(ni, nj)] > new_d:
                dists[(ni, nj)] = new_d
                q.put((new_d, (ni ,nj)))
                
    return None

def repeat_grid(grid, k = 5):
    g = np.array(grid) - 1
    grid = np.empty((0, len(g)*k), dtype = int)
    
    for _ in range(k):
        row = np.concatenate(tuple((g + i)%9 for i in range(k)), axis = 1)
        grid = np.concatenate((grid, row), axis = 0)
        g = (g + 1)%9
    grid += 1
    return grid

def day_15_p1():
    grid = day_15_input('day_15_input.txt')
    return shortest(grid, (0,0))

def day_15_p2():
    grid = day_15_input('day_15_input.txt')
    return shortest(repeat_grid(grid), (0, 0))

ic(day_15_p1())
ic(day_15_p2())