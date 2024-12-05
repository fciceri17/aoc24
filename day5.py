from collections import defaultdict
from pickletools import read_uint1

with open('input/day5.txt', 'r') as f:
     data=f.readlines()



# data='''47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13
#
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47'''.splitlines()


rules = defaultdict(set)
cases = []
for entry in data:
    clean = entry.strip()
    if not clean:
        continue
    elif '|' in clean:
        b, a = clean.strip().split('|')
        rules[b].add(a)
    else:
        cases.append(clean)

reverse_rules = defaultdict(set)
for b,a in rules.items():
    for v in a:
        reverse_rules[v].add(b)

result = []
bad_apples = []
for case in cases:
    full_case = case.split(',')
    for i, entry in enumerate(full_case):
        if i ==0: continue
        if any(e in rules[entry] for e in full_case[:i]):
            bad_apples.append(full_case)
            break
    else:
        result.append((full_case[len(full_case)//2]))
print(sum(int(x) for x in result))

def insert_in(case, v, rules):
    for i, entry in enumerate(list(case)):
        if entry in rules[v]:
            continue
        else:
            return case[:i] + [v] + case[i:]
    return case + [v]

p2 = 0
for case in bad_apples:
    new_case = []
    for e in case:
        new_case = insert_in(new_case, e, rules)
    p2+=int(new_case[len(new_case)//2])
print(p2)