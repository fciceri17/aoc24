with open('input/day9.txt', 'r') as f:
    data = f.read().strip()

# data = '''2333133121414131402'''

naive_unpack = []
disk_repr = dict(files=list(), free=list())
curr_head = 0
for i, v in enumerate(data):
    dist = int(v)
    if i % 2 == 0:
        naive_unpack += [f'{i // 2}'] * dist
        disk_repr['files'] += [[f'{i // 2}', dist, curr_head]]
    else:
        naive_unpack += ['.'] * dist
        disk_repr['free'] += [dist]
    curr_head += dist
new_unpack = list(naive_unpack)
curr_free = 0
for i, entry in enumerate(naive_unpack[::-1]):
    while curr_free < len(new_unpack) and new_unpack[curr_free] != '.':
        curr_free += 1
    if len(new_unpack) - i < curr_free:
        break
    new_unpack[curr_free] = entry
    new_unpack[len(new_unpack) - i - 1] = '.'


def get_checksum(unpacked):
    checksum = 0
    for i, v in enumerate(unpacked):
        if v == '.':
            continue
        checksum += i * int(v)
    return checksum


print(get_checksum(new_unpack))

p2_unpack = list(naive_unpack)


def next_free_block(disk_map, start_i):
    for i in range(start_i, len(disk_map)):
        if disk_map[i] == '.':
            for j in range(i, len(disk_map)):
                if disk_map[j] != '.':
                    break
            return i, j - i
    return None, None


for to_move in disk_repr['files'][::-1]:
    start, space = next_free_block(p2_unpack, 0)
    while space and space < to_move[1]:
        start, space = next_free_block(p2_unpack, start + space + 1)
    if not space or start > to_move[2]:
        continue
    for i in range(0, to_move[1]):
        p2_unpack[start + i] = to_move[0]
        p2_unpack[to_move[2] + i] = '.'
print(get_checksum(p2_unpack))
