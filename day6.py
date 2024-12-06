from typing import Tuple

with open('input/day6.txt', 'r') as f:
     data_in=f.readlines()
     data = [row.strip() for row in data_in]


# data='''....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...'''.splitlines()

def rotate(direction):
     if direction==(0,1):
          return 1, 0
     if direction == (1, 0):
          return 0, -1
     if direction == (0, -1):
          return -1, 0
     if direction == (-1, 0):
          return 0, 1


def move(curr_pos: Tuple[int, int], direction: Tuple[int, int], grid):
     next_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1])
     if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1]>= len(grid[0]):
         return None
     if grid[next_pos[0]][next_pos[1]] == '#':
          return curr_pos, rotate(direction)
     if grid[next_pos[0]][next_pos[1]] in ('.', '^') :
         return next_pos, direction
     raise Exception('unknown')

def get_visited(grid):
     start_pos = (0, 0)
     for i, row in enumerate(grid):
         for j, v in enumerate(row):
             if v == '^':
                  start_pos = (i, j)

     visited = {(start_pos, (-1,0))}
     next = move(start_pos, (-1, 0), grid)
     while next:
          if next in visited:
               raise Exception('loop')
          visited.add(next)
          next = move(*next, grid)
     return visited

print(len(set(x[0] for x in get_visited(data))))

obstacled = 0
for i, row in enumerate(data):
     for j, v in enumerate(row):
          if v == '.':
               temp_grid = data[:i]+[[row[n] if n!=j else '#' for n in range(len(row))]]+data[i+1:]
               try:
                    get_visited(temp_grid)
               except:
                    obstacled += 1
print(obstacled)