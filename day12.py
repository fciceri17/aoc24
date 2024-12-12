from collections import defaultdict
from functools import cache

with open('input/day12.txt', 'r') as f:
    data = f.read().splitlines()

# data='''RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE'''.splitlines()

map_ = {}
for i, entry in enumerate(data):
    for j, v in enumerate(entry):
        map_[(i, j)] = v

areas = {}
perims = {}
in_perimiter = {}
def flood_fill(loc, curr, start):
    areas[start] |= {loc}
    local_contrib = 4
    for dir in [(0,1), (0,-1), (1,0), (-1, 0)]:
        next_loc = (loc[0] + dir[0], loc[1] + dir[1])
        if next_loc in map_ and map_[next_loc] == curr:
            local_contrib -= 1
            if next_loc not in areas[start]:
                flood_fill(next_loc, curr, start)
    perims[start]+= local_contrib
    if local_contrib>0:
        in_perimiter[start] |= {loc}

for i, row in enumerate(data):
    for j, v in enumerate(row):
        if not any((i,j) in x for x in areas.values()):
            areas[(i,j)]={(i,j)}
            perims[(i, j)] = 0
            in_perimiter[(i, j)] = set()
            flood_fill((i, j), v, (i,j))
total=0
for begin in areas:
    total+=perims[begin]*len(areas[begin])
print(total)

def is_corner(corner, curr):
    outside = [i not in map_ for i in corner]
    if sum(outside)==3:
        return 3
    if sum(outside)==2:
        return 3 * (map_[corner[outside.index(False)]]!=curr)
    values = [map_[i] for i in corner]
    different = [v!=curr for v in values]
    if all(different):
        return 3
    if sum(different) == 1:
        return 1
    if sum(different) == 2 and values[1]==curr:
        return 3
    return 0

sides = {}
for start, contained in areas.items():
    corners = 0
    for part_of_side in contained:
        for corner1, corner2, corner3 in [
            ((-1,0),(-1, -1),(0,-1)),
            ((0,-1), (1,-1),(1,0)),
            ((1,0), (1,1), (0,1)),
            ((0,1), (-1,1), (-1, 0))
        ]:
            corner = ((part_of_side[0] + corner1[0], part_of_side[1] + corner1[1]),
                      (part_of_side[0] + corner2[0], part_of_side[1] + corner2[1]),
                      (part_of_side[0] + corner3[0], part_of_side[1] + corner3[1]))
            corners+=is_corner(corner, map_[part_of_side])
    sides[start]=corners//3
total=0
for begin in areas:
    total+=sides[begin]*len(areas[begin])
print(total)
