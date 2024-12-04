from aocd import get_data
input = get_data(day=4, year=2024).splitlines()
import itertools

# WRITE YOUR SOLUTION HERE
def dfs(graph, start):
    password = 'XMAS'
    i, j, main_dir = start
    to_visit = [(i, j, 1, main_dir)]
    sol = []
    DIRECTIONS = list(itertools.product(range(-1, 2), repeat=2))

    while to_visit:
        i, j, c, dir = to_visit.pop()
        di, dj = DIRECTIONS[dir]
        ni, nj = i + di, j + dj
        if 0 <= ni < len(graph) and 0 <= nj < len(graph[0]) and graph[ni][nj] == password[c]:
            if c == 3:
                sol.append((ni, nj, main_dir))
            else:
                to_visit.append((ni, nj, c + 1, main_dir))
    return sol

def part_1(lines):
    cnt = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'X':
                for d in range(9):
                    cnt += len(dfs(lines, (i, j, d)))
    return cnt

def chech_4_Xmas(graph, start):
    i, j = start
    diags = []
    for (di, dj) in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(graph) and 0 <= nj < len(graph[0]):
            diags.append(graph[ni][nj])

    Xmas = ''.join(diags)
    return (Xmas == 'MMSS' or Xmas == 'SMMS' or Xmas == 'SSMM' or Xmas == 'MSSM')

def part_2(lines):
    cnt = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'A':
                cnt += chech_4_Xmas(lines, (i, j))
    return cnt

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
