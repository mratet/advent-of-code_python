
lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE
import collections

def part_1(lines):

    len_basis = 10

    basis = {(x, y): (0, -1) for x in range(len_basis) for y in range(len_basis)}

    bricks = []
    for line in lines:
        start, end = line.split('~')
        start = [int(c) for c in start.split(',')]
        end = [int(c) for c in end.split(',')]
        bricks.append([start, end])

    bricks.sort(key=lambda x: x[0][2])
    is_supported_by = [[] for _ in range(len(bricks) + 1)]

    for i, [(x_s, y_s, z_s), (x_e, y_e, z_e)] in enumerate(bricks):
        if x_s == x_e and y_s == y_e:
            is_supported_by[i + 1].append(basis[(x_e, y_e)][1])
            basis[(x_s, y_s)] = (basis[(x_s, y_s)][0] + z_e - z_s + 1, i)

        elif x_s == x_e:
            z_max = max([basis[(x_e, y)][0] for y in range(y_s, y_e + 1)])
            for y in range(y_s, y_e + 1):
                if basis[(x_e, y)][0] == z_max and basis[(x_e, y)][1] not in is_supported_by[i + 1] :
                    is_supported_by[i + 1].append(basis[(x_e, y)][1])
                basis[(x_e, y)] = (z_max + 1, i)

        elif y_s == y_e:
            z_max = max([basis[(x, y_e)][0] for x in range(x_s, x_e + 1)])
            for x in range(x_s, x_e + 1):
                if basis[(x, y_e)][0] == z_max and basis[(x, y_e)][1] not in is_supported_by[i + 1]:
                    is_supported_by[i + 1].append(basis[(x, y_e)][1])
                basis[(x, y_e)] = (z_max + 1, i)
        else:
            print('There are square in the input !')

    not_safe = [False for _ in range(len(bricks))]

    for tab in is_supported_by:
        if len(tab) == 1 and tab[0] != -1:
            not_safe[tab[0]] = True


    return len(bricks) - sum(not_safe)

def part_2(lines):
    len_basis = 10

    basis = {(x, y): (0, -1) for x in range(len_basis) for y in range(len_basis)}

    bricks = []
    for line in lines:
        start, end = line.split('~')
        start = [int(c) for c in start.split(',')]
        end = [int(c) for c in end.split(',')]
        bricks.append([start, end])

    bricks.sort(key=lambda x: x[0][2])

    is_supported_by = [[] for _ in range(len(bricks) + 1)]

    for i, [(x_s, y_s, z_s), (x_e, y_e, z_e)] in enumerate(bricks):
        if x_s == x_e and y_s == y_e:
            is_supported_by[i + 1].append(basis[(x_e, y_e)][1])
            basis[(x_s, y_s)] = (basis[(x_s, y_s)][0] + z_e - z_s + 1, i)

        elif x_s == x_e:
            z_max = max([basis[(x_e, y)][0] for y in range(y_s, y_e + 1)])
            for y in range(y_s, y_e + 1):
                if basis[(x_e, y)][0] == z_max and basis[(x_e, y)][1] not in is_supported_by[i + 1]:
                    is_supported_by[i + 1].append(basis[(x_e, y)][1])
                basis[(x_e, y)] = (z_max + 1, i)

        elif y_s == y_e:
            z_max = max([basis[(x, y_e)][0] for x in range(x_s, x_e + 1)])
            for x in range(x_s, x_e + 1):
                if basis[(x, y_e)][0] == z_max and basis[(x, y_e)][1] not in is_supported_by[i + 1]:
                    is_supported_by[i + 1].append(basis[(x, y_e)][1])
                basis[(x, y_e)] = (z_max + 1, i)
        else:
            print('There are square in the input !')

    not_safe = [False for _ in range(len(bricks))]
    print(is_supported_by)

    for tab in is_supported_by:
        if len(tab) == 1 and tab[0] != -1:
            not_safe[tab[0]] = True

    support = [[] for _ in range(len(bricks) + 1)]
    for i, tab in enumerate(is_supported_by):
        for neighboor in tab:
            if neighboor != -1:
                support[neighboor + 1].append(i)
    ans = 0
    print(support)
    for i in range(len(not_safe)):
        if not_safe[i]:
            ans += dfs(i + 1, support)

    return ans
# END OF SOLUTION

def dfs(start, graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    q = collections.deque()
    q.append(start)
    while q:
        node = q.popleft()
        visited[node] = True
        for neighboor in graph[node]:
            if not visited[neighboor]:
                q.append(neighboor)

    return sum(visited) - 1





test_input = open('input-test.txt').read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == '-':
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f'My answer on test set for the first problem is {part_1(test_lines)}')
print(solution)
print(f'My answer is {part_1(lines)}')

print(f'My answer on test set for the second problem is {part_2(test_lines)}')
print(f'My answer is {part_2(lines)}')
