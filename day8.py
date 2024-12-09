from collections import defaultdict
with open('input/day8.txt', 'r') as f:
     data=f.read().splitlines()

# data = '''............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............'''.splitlines()

def in_bounds(data, i, j):
     max_i = len(data)
     max_j = len(data[0])
     if i<0 or i>=max_i or j < 0 or j >= max_j:
         return False
     return True

locations = defaultdict(list)
for i, row in enumerate(data):
     for j, value in enumerate(row):
          if value!='.':
               locations[value].append((i,j))

antinodes = defaultdict(set)
for antenna_type, antennae in locations.items():
     for i, base in enumerate(antennae):
          for other_base in antennae[i+1:]:
               dx = other_base[0] - base[0]
               dy = other_base[1] - base[1]
               loc1 = (base[0]-dx, base[1] - dy)
               loc2 = (other_base[0] + dx, other_base[1] + dy)
               if in_bounds(data, loc1[0], loc1[1]):
                   antinodes[antenna_type].add(loc1)
               if in_bounds(data, loc2[0], loc2[1]):
                    antinodes[antenna_type].add(loc2)
print(len(set(x for y in antinodes.values() for x in y)))

antinodes2 = defaultdict(set)
for antenna_type, antennae in locations.items():
     for i, base in enumerate(antennae):
          antinodes2[antenna_type].add(base)
          for other_base in antennae[i+1:]:
               dx = other_base[0] - base[0]
               dy = other_base[1] - base[1]
               loc1 = (base[0]-dx, base[1] - dy)
               while in_bounds(data, loc1[0], loc1[1]):
                   antinodes2[antenna_type].add(loc1)
                   loc1 = (loc1[0] - dx, loc1[1] - dy)
               loc2 = (other_base[0] + dx, other_base[1] + dy)
               while in_bounds(data, loc2[0], loc2[1]):
                    antinodes2[antenna_type].add(loc2)
                    loc2 = (loc2[0] + dx, loc2[1] + dy)
print(len(set(x for y in antinodes2.values() for x in y)))
