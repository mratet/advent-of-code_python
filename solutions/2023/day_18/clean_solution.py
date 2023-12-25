from aocd import get_data
input = get_data(day=18, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE

N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)
dir_dict = {
    'U': N,
    'D': S,
    'R': E,
    'L': W,
}

second_dir_dict = {
    '0': E,
    '1': N,
    '2': W,
    '3': S,
}

def shoelace_area(points):
    area = 0
    for i in range(len(points) - 1):
        area += points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1]
    return area // 2

def _parse(input, part):
    perimeter, points, point = 0, [], (0, 0)

    for line in input:
        direction, distance, hexa = line.split()
        if part == 'part_2':
            direction, distance = second_dir_dict[hexa[-2]], int(hexa[2:-2], 16)
        else:
            direction = dir_dict[direction]
            distance = int(distance)

        point = (point[0] + distance * direction[0], point[1] + distance * direction[1])
        perimeter += distance
        points.append(point)

    return points, perimeter

def part_1(input):
    points, perimeter = _parse(input, 'part_1')
    area = shoelace_area(points)
    return abs(area) + perimeter // 2 + 1

def part_2(input):
    points, perimeter = _parse(input, 'part_2')
    area = shoelace_area(points)
    return abs(area) + perimeter // 2 + 1
# END OF SOLUTION


print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
