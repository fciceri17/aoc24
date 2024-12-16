import math

with open('input/day14.txt', 'r') as f:
    data = f.read().splitlines()

# data='''p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3'''.splitlines()

robots = []
for entry in data:
    p,v = entry.split()
    robot = {
        'p': [int(x) for x in p[2:].split(',')],
        'v': [int(x) for x in v[2:].split(',')]
    }
    robots.append(robot)

# grid_size = 11, 7
grid_size = 101, 103

def pos_after_x(robot, seconds, grid_size):
    x0,y0 = robot['p']
    vx, vy = robot['v']
    return (x0 + vx * seconds)%grid_size[0], (y0 + vy * seconds)%grid_size[1]

future_bots = [pos_after_x(bot, 100, grid_size) for bot in robots]

midpoints = grid_size[0]//2, grid_size[1] // 2

def in_quadrant(bots, cx, cy):
    return sum([cx(bot[0]) and cy(bot[1]) for bot in bots])

q1 = in_quadrant(future_bots, lambda x: x < midpoints[0], lambda y: y < midpoints[1])
q2 = in_quadrant(future_bots, lambda x: x > midpoints[0], lambda y: y < midpoints[1])
q3 = in_quadrant(future_bots, lambda x: x < midpoints[0], lambda y: y > midpoints[1])
q4 = in_quadrant(future_bots, lambda x: x > midpoints[0], lambda y: y > midpoints[1])

print(math.prod([q1,q2,q3,q4]))

def view_grid(robots):
    grid = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]
    for bot in robots:
        grid[bot[1]]=[x+1 if i==bot[0] else x for i,x in enumerate(grid[bot[1]])]
    tcol = has_col(grid, 10)
    if tcol:
        print('\n'.join(''.join('.' if x==0 else '#' for x in v) for v in grid))
        print(tcol)
        print('')
        return 1

def has_col(grid, length):
    colmax=(-1,-1)
    for i in range(len(grid[0])):
        curr=0
        for j in range(len(grid)):
            if grid[j][i] != 0:
                curr+=1
            else:
                if curr > colmax[0]:
                    colmax = (i, curr)
                curr=0
    if colmax[1]>= length:
        return colmax[0]

for i in range(100000):
    if(view_grid([pos_after_x(bot,i, grid_size) for bot in robots])):
        break
print(i)