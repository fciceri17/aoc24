with open('input/day10.txt', 'r') as f:
    data = f.read().splitlines()

# data='''89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732'''.splitlines()


map_ = [[int(x) if x!='.' else 1 for x in y] for y in data]

trailheads = set()
for i,row in enumerate(map_):
    for j, v in enumerate(row):
        if v == 0:
            trailheads.add((i,j))


def in_bounds(map_, i, j):
    max_i = len(map_)
    max_j = len(map_[0])
    if i < 0 or i >= max_i or j < 0 or j >= max_j:
        return False
    return True

def find_neighbors(location, map_):
    neighbors = set()
    for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if in_bounds(map_, location[0] + i, location[1] + j) and map_[location[0] + i][location[1] + j] == map_[location[0]][location[1]]+1:
            neighbors.add((location[0] + i, location[1] + j))
    return neighbors


def search(location, map_):
    if map_[location[0]][location[1]] == 9:
        return [location]
    else:
        potential = find_neighbors(location, map_)
        if not potential:
            return []
        else:
            to_return = [search(x, map_) for x in potential]
            return sum(to_return, [])

scores = dict()
scores2 = dict()
for trailhead in trailheads:
    reached = search(trailhead, map_)
    scores[trailhead] = len(set(reached))
    scores2[trailhead] = len(reached)
print(sum(scores.values()))
print(sum(scores2.values()))