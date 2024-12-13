from dataclasses import dataclass

from mpmath.libmp.libelefun import machin

with open('input/day13.txt', 'r') as f:
    data = f.read()

# data='''Button A: X+94, Y+34
# Button B: X+22, Y+67
# Machine: X=8400, Y=5400
#
# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Machine: X=12748, Y=12176
#
# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Machine: X=7870, Y=6450
#
# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Machine: X=18641, Y=10279'''

@dataclass
class XY:
    x: int
    y: int

@dataclass
class Machine:
    a : XY
    b : XY
    prize: XY

solves = [[], []]

machines = []
for input_ in data.split('\n\n'):
    rows = input_.splitlines()
    a = rows[0].split(': ')[-1].split(',')
    b = rows[1].split(': ')[-1].split(',')
    prize = rows[2].split(': ')[-1].split(',')
    machines.append(Machine(XY(int(a[0].split('+')[-1]), int(a[1].split('+')[-1])), XY(int(b[0].split('+')[-1]), int(b[1].split('+')[-1])), XY(int(prize[0].split('=')[-1]), int(prize[1].split('=')[-1]))))

def solve(machines):
    cost = 0
    for i,machine in enumerate(machines):
        max_b = min(machine.prize.x // machine.b.x, machine.prize.y // machine.b.y)
        max_a = min(machine.prize.x // machine.a.x, machine.prize.y // machine.a.y)
        a_count = 0
        b_count = max_b
        curr = (b_count * machine.b.x, b_count * machine.b.y)
        while curr != (machine.prize.x, machine.prize.y) and b_count > 0 and a_count < max_a:
            if curr[0] >= machine.prize.x or curr[1] >= machine.prize.y:
                curr = (curr[0] - machine.b.x, curr[1] - machine.b.y)
                b_count -= 1
            else:
                curr = (curr[0] + machine.a.x, curr[1] + machine.a.y)
                a_count += 1
        solves[0].append((a_count, b_count, curr))
        if curr == (machine.prize.x, machine.prize.y):
            cost += a_count * 3 + b_count
    return cost

print(solve(machines))
harder_prizes = [Machine(x.a, x.b, XY(10000000000000 + x.prize.x, 10000000000000 + x.prize.y)) for x in machines]

def solve_single(machine: Machine):

    def rounded(f):
        if f % 1 > 0.5:
            return int(f)+1
        return int(f)
    # a * ax + b * bx = px
    # a * ay + b * by = py

    # a = px / ax - b * bx / ax
    # a = py / ay - b * by / ay

    # px / ax - b * bx / ax = py / ay - b * by / ay
    # b * by/ay - b * bx / ax = py / ay - px / ax
    # b * (by/ay - bx / ax) = py / ay - px / ax
    b = (machine.prize.y / machine.a.y - machine.prize.x / machine.a.x) / (machine.b.y/ machine.a.y - machine.b.x / machine.a.x)

    if abs(rounded(b) - b) > 0.0001 or b < 0:
        return 0
    b = rounded(b)
    a = rounded(machine.prize.y / machine.a.y - b * machine.b.y / machine.a.y)
    if a >0:
        solves[1].append((a, b))
        return a * 3 + b
    else:
        return 0

solutions = [solve_single(m) for m in harder_prizes]
print(sum(solutions))