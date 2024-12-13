from aocd import get_data, submit
input = get_data(day=13, year=2024).split('\n\n')
import re

# WRITE YOUR SOLUTION HERE
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def decomposition(Xa, Ya, Xb, Yb, Xc, Yc):
    cand = []
    for i in range(100):
        for j in range(100):
            X_cand = Xa * i + Xb * j
            Y_cand = Ya * i + Yb * j
            if int(X_cand) == Xc and int(Y_cand) == Yc:
                cand.append(3 * i + j)
    if cand:
        return min(cand)
    else:
        return 0

def fast_decomposition(Xa, Ya, Xb, Yb, Xc, Yc):
    X = abs(Xa * Yc - Ya * Xc)
    Y = abs(Yb * Xc - Xb * Yc)
    P = pgcd(X, Y)
    X //= P
    Y //= P
    for k in range(1000):
        if Xa * (k * Y) + Xb * (k * X) == Xc:
            return k * (3 * Y + X)
    return 0

def part_1(lines):
    score = 0
    for line in lines:
        line = line.split('\n')
        Xa, Ya = map(int, re.findall(r'(\d+)', line[0]))
        Xb, Yb = map(int, re.findall(r'(\d+)', line[1]))
        Xc, Yc = map(int, re.findall(r'(\d+)', line[2]))
        score += decomposition(Xa, Ya, Xb, Yb, Xc, Yc)
    return score

def part_2(lines):
    score = 0
    for line in lines:
        line = line.split('\n')
        Xa, Ya = map(int, re.findall(r'(\d+)', line[0]))
        Xb, Yb = map(int, re.findall(r'(\d+)', line[1]))
        Xc, Yc = map(int, re.findall(r'(\d+)', line[2]))
        Xc = Xc + 10000000000000
        Yc = Yc + 10000000000000
        score += fast_decomposition(Xa, Ya, Xb, Yb, Xc, Yc)
    return score

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
