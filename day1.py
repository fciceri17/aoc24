l1,l2 = [], []
with open('input/day1.txt', 'r') as f:
     data=f.readlines()

# data = '''3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3'''.splitlines()

for row in data:
    v1,v2 = row.split()
    l1.append(int(v1))
    l2.append(int(v2))

print(sum(abs(b-a) for a,b in zip(sorted(l1), sorted(l2))))

freq = {x:l2.count(x) for x in set(l2)}
print(sum(x*freq.get(x,0) for x in l1))