from aocd import get_data, submit
input = get_data(day=3, year=2019).splitlines()
# WRITE YOUR SOLUTION HERE
def get_wire_path(insts):
    x, y = 0, 0
    path = []
    for inst in insts:
        op, val = inst[0], int(inst[1:])
        for _ in range(val):
            if op == 'R':
                y += 1
            elif op == 'L':
                y -= 1
            elif op == 'U':
                x -= 1
            elif op == 'D':
                x += 1
            path.append((x, y))
    return path

def part_1(lines):
    wire1, wire2 =  lines[0], lines[1]
    path1, path2 = get_wire_path(wire1.split(',')), get_wire_path(wire2.split(','))
    crossed_pos = set(path1) & set(path2)
    return min(abs(x) + abs(y) for (x, y) in crossed_pos)

def part_2(lines):
    wire1, wire2 =  lines[0], lines[1]
    path1, path2 = get_wire_path(wire1.split(',')), get_wire_path(wire2.split(','))
    crossed_pos = set(path1) & set(path2)
    return min(path1.index(pos) + path2.index(pos) + 2 for pos in crossed_pos)


# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')

