with open('input/day4.txt', 'r') as f:
     data=f.readlines()

# data='''MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX'''.splitlines()

def find_horizontal(entries):
    found = 0
    for row in entries:
        cols = len(row)
        for i in range(cols):
            if i + 4 <= cols and (row[i:i + 4] == 'XMAS' or row[i:i + 4] == 'SAMX'):
                found += 1
    return found

def find_diagonal(entries):
    found = 0
    rows = len(entries)
    cols = len(entries[0])
    for i, row in enumerate(entries):
        for j, v in enumerate(row):
            if v=='X':
                if j+4 <= cols and i+4 <= rows and entries[i+1][j+1] == 'M'and entries[i+2][j+2] == 'A' and entries[i+3][j+3] == 'S':
                    found+=1
                if j-3 >= 0 and i-3 >= 0 and entries[i-1][j-1] == 'M'and entries[i-2][j-2] == 'A' and entries[i-3][j-3] == 'S':
                    found+=1
                if j+4 <= cols and i-3>=0 and entries[i-1][j+1] == 'M'and entries[i-2][j+2] == 'A' and entries[i-3][j+3] == 'S':
                    found+=1
                if j-3 >= 0 and i+4 <= rows and entries[i+1][j-1] == 'M'and entries[i+2][j-2] == 'A' and entries[i+3][j-3] == 'S':
                    found+=1
    return found




# horizontal
hor = find_horizontal(data)
diag = find_diagonal(data)

# transpose and search again
transposed = [''.join(list(x)) for x in zip(*data)]
ver = find_horizontal(transposed)
print(hor+ver+diag)

crossed = 0
for i, row in enumerate(data):
    if i == len(data)-1 or i == 0 :
        continue
    for j, v in enumerate(row):
        if j == 0 or j == len(row)-1:
            continue
        if v == 'A':
            ul = False
            ur = False
            # look up-left and down-right
            if (data[i-1][j-1],data[i+1][j+1]) in [('S', 'M'), ('M', 'S')]:
                # now up-right and down-left
                if (data[i + 1][j - 1], data[i - 1][j + 1]) in [('S', 'M'), ('M', 'S')]:
                    crossed+=1
print(crossed)