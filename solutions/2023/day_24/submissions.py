import itertools

lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE
import numpy as np
from scipy.optimize import minimize

def find_intersection_2d(a1, a2):
    p1, v1 = a1[0:2], a1[3:5]
    p2, v2 = a2[0:2], a2[3:5]

    p1, v1 = p1.reshape((2, 1)), v1.reshape((2, 1))
    p2, v2 = p2.reshape((2, 1)), v2.reshape((2, 1))

    A = np.hstack((v1, -v2))
    b = p2 - p1

    try:
        solution = np.linalg.solve(A, b)
        t, s = solution[0][0], solution[1][0]
        print(a1[:3] + t * a1[3:])
        print(a2[:3] + s * a2[3:])
        return t, s, (p1 + t * v1).reshape((1, 2))

    except np.linalg.LinAlgError:
        # Singular system
        return -1, 0, 0

def _parse(input):
    asteroids = []
    for line in input:
        pos, spd = line.split('@')
        pos = [int(c) for c in pos.split(',')]
        spd = [int(c) for c in spd.split(',')]
        asteroids.append(pos + spd)
    asteroids = np.array(asteroids)
    return asteroids

def part_1(lines):
    asteroids = _parse(lines)
    n = len(asteroids)

    ans = 0
    min_val = 200000000000000
    max_val = 400000000000000

    for i in range(n):
        for j in range(i + 1, n):
            s, t, intersection = find_intersection_2d(asteroids[i], asteroids[j])
            if s >= 0 and t >= 0 and min_val <= intersection[0][0] <= max_val and min_val <= intersection[0][1] <= max_val:
                ans += 1
    return ans

def part_2(lines):
    asteroids = _parse(lines)

    def shortest_distance(x):

        p1, v1 = x[:3], x[3:]
        distance = 0

        for a in asteroids[:3]:
            p2, v2 = a[:3], a[3:]

            n = np.cross(v1, v2)

            n1 = np.cross(v1, n)
            n2 = np.cross(v2, n)

            if v1 @ n2 == 0:
                continue

            c1 = p1 + (p2 - p1) @ n2 / (v1 @ n2) * v1
            c2 = p2 + (p1 - p2) @ n1 / (v2 @ n1) * v1

            distance += np.linalg.norm(c1 - c2)

        return distance

    n = len(asteroids)
    x0 = np.array([24, 13, 10, -3, 1, 2])
    result = minimize(shortest_distance, x0)
    print(result)

    return 0
# END OF SOLUTION


test_input = open('input-test.txt').read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == '-':
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f'My answer on test set for the first problem is {part_1(test_lines)}')
print(solution)
# print(f'My answer is {part_1(lines)}')

print(f'My answer on test set for the second problem is {part_2(test_lines)}')
# print(f'My answer is {part_2(lines)}')
