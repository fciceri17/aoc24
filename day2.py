l1,l2 = [], []
with open('input/day2.txt', 'r') as f:
     data=f.readlines()

# data = '''7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9'''.splitlines()

def check_safe(readings):
    expected = [int(x) for x in readings]
    sort = sorted(expected)
    if sort != expected:
        sort = sort[::-1]
    if sort == expected:
        prev = None
        for entry in sort:
            if not prev:
                prev = entry
            else:
                if abs(entry - prev) > 3 or entry == prev:
                    break
                prev = entry
        else:
            return True

safe_idx = {i for i, report in enumerate(data) if check_safe(report.split())}

print(len(safe_idx), safe_idx)

now_safe = set()
for i, report in enumerate(data):
    if i not in safe_idx:
        to_check = [int(x) for x in report.split()]
        for skip in range(0, len(to_check)):
            if check_safe([x for j,x in enumerate(to_check) if j != skip]):
                now_safe.add(i)
                break
print(len(safe_idx.union(now_safe)))