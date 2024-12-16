import heapq
from collections import defaultdict

import numpy as np

with open('input/day16.txt', 'r') as f:
    data = f.read()

# data='''#################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################'''

data = data.splitlines()
directions = {
    '^': (-1, 0),
    '<': (0, -1),
    'v': (1, 0),
    '>': (0, 1)

}
def explore(data):
    visited_nodes = set()
    def graph_next(location):
        ret = {}
        for direction in ('^', '>', 'v', '<'):
            if location[-1]!= direction:
                ret[(location[0], location[1], direction)] = 1000
            else:
                dir = directions[direction]
                next_loc = location[0]+ dir[0], location[1] + dir[1]
                if data[next_loc[0]][next_loc[1]] != '#' and (next_loc[0], next_loc[1]):
                    ret[(next_loc[0], next_loc[1], direction)] = 1
        return ret
    queue = []
    at_ = len(data)-2, 1, '>'
    end = 1, len(data[0])-2
    cost = {at_:0}
    result_set = []
    prev = defaultdict(set)
    while at_[:2]!=end:
        # explore neighbors
        visited_nodes.add(at_)
        neighbors = graph_next(at_)
        for neighbor, add in neighbors.items():
            if cost.get(neighbor,np.inf) >= cost[at_]+add:
                prev[neighbor].add(at_)
                cost[neighbor] = cost[at_] + add
                heapq.heappush(queue, (cost[neighbor], neighbor))
        at_ = heapq.heappop(queue)[1]
    result_set.append(at_)
    while True:
        potential_at = heapq.heappop(queue)[1]
        if potential_at[:2]==end:
            result_set.append(potential_at)
        else: break
    return cost[at_], prev, result_set

cheapest, prev, end_nodes = explore(data)
print(cheapest)

total_in_path = set()
while end_nodes:
    node = end_nodes.pop()
    total_in_path.add(node[:2])
    prev_nodes = prev[node]
    end_nodes.extend(prev_nodes)
print(len(total_in_path))