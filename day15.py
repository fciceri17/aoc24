from dataclasses import dataclass

from mpmath.libmp.libelefun import machin

with open('input/day15.txt', 'r') as f:
    data = f.read()

# data='''##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########
#
# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''

to_decode, sequences = data.split('\n\n')
start = (-1,-1)
map_ = {}
rows = len(to_decode.splitlines())
cols = len(to_decode.splitlines()[0])
for i, line in enumerate(to_decode.splitlines()):
    for j, char in enumerate(line):
        map_[(i, j)] = char
        if char == '@':
            start = (i,j)

steps = ''.join(sequences.splitlines())

def push(input_map, from_, direction):
    if direction==(-1,0):
        first_space = -1
        for i in range(from_[0], -1, -1):
            if input_map[(i, from_[1])] == '.':
                first_space = i
                break
            if input_map[(i, from_[1])] == '#':
                break
        if first_space == -1:
            return from_
        for j in range(first_space, from_[0]):
            input_map[(j, from_[1])] = input_map[(j + 1, from_[1])]
    elif direction==(1,0):
        first_space = -1
        for i in range(from_[0], rows):
            if input_map[(i, from_[1])] == '.':
                first_space = i
                break
            if input_map[(i, from_[1])] == '#':
                break
        if first_space == -1:
            return from_
        for j in range(first_space, from_[0], -1):
            input_map[(j, from_[1])] = input_map[(j - 1, from_[1])]
    elif direction == (0, -1):
        first_space = -1
        for i in range(from_[1], -1, -1):
            if input_map[(from_[0], i)] == '.':
                first_space = i
                break
            if input_map[(from_[0], i)] == '#':
                break
        if first_space == -1:
            return from_
        for j in range(first_space, from_[1]):
            input_map[(from_[0], j)] = input_map[(from_[0], j + 1)]
    elif direction == (0, 1):
        first_space = -1
        for i in range(from_[1], cols):
            if input_map[(from_[0], i)] == '.':
                first_space = i
                break
            if input_map[(from_[0], i)] == '#':
                break
        if first_space == -1:
            return from_
        for j in range(first_space, from_[1],-1):
            input_map[(from_[0], j)] = input_map[(from_[0], j - 1)]

    input_map[from_] = '.'
    return from_[0] + direction[0], from_[1] + direction[1]

curr_pos = start
directions = {
    '^': (-1, 0),
    '<': (0, -1),
    'v': (1, 0),
    '>': (0, 1)

}
for step in steps:
    curr_pos = push(map_, curr_pos, directions[step])

print(sum(x*100+y for x, y in map_.keys() if map_[(x, y)] == 'O'))

# new map lazily
map_={}
for i, line in enumerate(to_decode.splitlines()):
    new_line = line.replace('.', '..').replace('#', '##').replace('O', '[]').replace('@', '@.')
    for j, char in enumerate(new_line):
        map_[(i, j)] = char
        if char == '@':
            start = (i,j)

def push2(input_map, from_, direction):
    if direction==(-1,0):
        width_stack = [[from_[1]]]
        for i in range(from_[0]-1, -1, -1):
            can_proceed = True
            next_stack = set()
            empty = True
            for w in width_stack[-1]:
                if input_map[(i, w)] == '.':
                    next_stack.add(i)
                elif input_map[(i, w)] == '#':
                    can_proceed=False
                    break
                elif input_map[(i, w)] == '[':
                    empty=False
                    next_stack.add(w)
                    next_stack.add(w+1)
                elif input_map[(i, w)] == ']':
                    empty=False
                    next_stack.add(w)
                    next_stack.add(w-1)
            if empty or not can_proceed:
                break
            else:
                width_stack.append(next_stack)
        if not can_proceed:
            return from_
        for d,  layer in enumerate(width_stack[::-1]):
            # move layers up
            i = from_[0]-len(width_stack)+d
            for j in layer:
                input_map[(i, j)] = input_map[(i+1,j)]
                input_map[(i+1, j)] = '.'
    elif direction==(1,0):
        width_stack = [[from_[1]]]
        for i in range(from_[0]+1, rows):
            can_proceed = True
            next_stack = set()
            empty = True
            for w in width_stack[-1]:
                if input_map[(i, w)] == '.':
                    pass
                elif input_map[(i, w)] == '#':
                    can_proceed = False
                    break
                elif input_map[(i, w)] == '[':
                    empty = False
                    next_stack.add(w)
                    next_stack.add(w + 1)
                elif input_map[(i, w)] == ']':
                    empty = False
                    next_stack.add(w)
                    next_stack.add(w - 1)
            if empty or not can_proceed:
                break
            else:
                width_stack.append(next_stack)
        if not can_proceed:
            return from_
        for d, layer in enumerate(width_stack[::-1]):
            # move layers down
            i = from_[0] + len(width_stack) - d
            for j in layer:
                input_map[(i, j)] = input_map[(i - 1, j)]
                input_map[(i - 1, j)] = '.'
    elif direction == (0, -1):
        first_space = -1
        for i in range(from_[1], -1, -1):
            if input_map[(from_[0], i)] == '.':
                first_space = i
                break
            if input_map[(from_[0], i)] == '#':
                break
        if first_space == -1:
            return from_
        for j in range(first_space, from_[1]):
            input_map[(from_[0], j)] = input_map[(from_[0], j + 1)]
    elif direction == (0, 1):
        first_space = -1
        for i in range(from_[1], cols):
            if input_map[(from_[0], i)] == '.':
                first_space = i
                break
            if input_map[(from_[0], i)] == '#':
                break
        if first_space == -1:
            return from_
        for j in range(first_space, from_[1],-1):
            input_map[(from_[0], j)] = input_map[(from_[0], j - 1)]

    input_map[from_] = '.'
    return from_[0] + direction[0], from_[1] + direction[1]

def printmap():
    for i in range(rows):
        out_str=''
        for j in range(cols):
            out_str+=map_[(i,j)]
        print(out_str)

cols*=2
for i, step in enumerate(steps):
    start = push2(map_, start, directions[step])
    # printmap()
print(sum(x*100+y for x, y in map_.keys() if map_[(x, y)] == '['))
