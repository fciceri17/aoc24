import re
with open('input/day3.txt', 'r') as f:
     data=f.read()

# data='''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

groups = re.findall(r'''(?:mul\((\d+,\d+)\)|(do(n't)?)\(\))''', data)
roll = 0
roll2 = 0
active = True
for entry in groups:
    num, do, nt = entry
    if num:
        a, b = num.split(',')
        add = int(a) * int(b)
        roll+=add
        if active:
            roll2 += add
    elif nt:
        active = False
    elif do:
        active = True

print(roll)
print(roll2)