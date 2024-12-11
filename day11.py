from collections import defaultdict
from functools import cache

with open('input/day11.txt', 'r') as f:
    data = f.read().split()

# data = '''125 17'''.split()

ints = [int(x) for x in data]
int_counts = {x:ints.count(x) for x in set(ints)}

@cache
def next_int(i):
    if i == 0:
        return [1]
    else:
        rep = str(i)
        if len(rep) % 2 == 0:
            split = len(rep) // 2
            return[int(rep[:split]), int(rep[split:])]
        return [i * 2024]

for cc in range(75):
    next_count = defaultdict(int)
    for i in int_counts:
        future = next_int(i)
        for v in future:
            next_count[v]+=int_counts[i]
    int_counts=next_count
    if cc==24:
        print(sum(next_count.values()))
print(sum(next_count.values()))