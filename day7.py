import math

with open('input/day7.txt', 'r') as f:
     data=f.read().splitlines()


# data='''190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20'''.splitlines()

def attempt(result, curr_value, terms):
     if terms:
          return attempt(result, curr_value + terms[0], terms[1:]) or attempt(result, curr_value * terms[0], terms[1:])
     return result == curr_value

def concat(int1, int2):
     return int1*10**(int(math.log10(int2))+1)+int2

def attempt2(result, curr_value, terms):
     if terms:
          return attempt2(result, curr_value + terms[0], terms[1:]) or attempt2(result, curr_value * terms[0], terms[1:]) or attempt2(result, concat(curr_value, terms[0]), terms[1:])
     return result == curr_value

inp = {int(x.split(':')[0]): [int(y) for y in x.split(':')[-1].split()] for x in data}

print(sum(k for k, y in inp.items() if attempt(k, y[0], y[1:])))
print(sum(k for k, y in inp.items() if attempt2(k, y[0], y[1:])))
