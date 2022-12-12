import numpy as np 
import networkx as nx

def day_12_input(filename):
    with open(filename) as f:
        data = np.array([[*x.strip()] for x in f.readlines()])
    return data

grid = day_12_input('/home/romain/Documents/advent_of_code/2022/day_12_input.txt')

start = tuple(*np.argwhere(grid=='S'))
grid[start] = 'a'
end = tuple(*np.argwhere(grid=='E'))
grid[end] = 'z'

# Need it directed to be browsed to find a shortest path.
N = nx.grid_2d_graph(*grid.shape).to_directed()

# Conversion to show allowed paths. Condition is that neighbour nodes are accessible if their values are lower or plus 1 compared to current node
G = nx.DiGraph([(a,b) for a,b in N.edges() 
                if ord(grid[b]) <= ord(grid[a])+1])

# Dijkstra's algorithm to find shortest path from starting point in graph to end point
part1 = nx.shortest_path_length(G, source=start, target=end, method='dijkstra')
print(part1)

# Dijkstra from any point in graph to end.
part2 = nx.shortest_path_length(G, target=end, method='dijkstra')
part2 = min(part2[a] for a in part2 if grid[a]=='a')
print(part2)