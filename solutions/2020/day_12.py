from aocd import get_data

input = get_data(day=12, year=2020).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    x, y = 0, 0
    boat_orientation = 0

    for line in lines:
        action, n = line[0], int(line[1:])
        match action:
            case "N":
                x += n
            case "S":
                x -= n
            case "W":
                y -= n
            case "E":
                y += n
            case "L":
                boat_orientation -= n
            case "R":
                boat_orientation += n
            case "F":
                match (boat_orientation // 90) % 4:
                    case 0:
                        y += n
                    case 1:
                        x -= n
                    case 2:
                        y -= n
                    case 3:
                        x += n
    return abs(x) + abs(y)


def part_2(lines):
    x, y = 0, 0
    wx, wy = 1, 10

    for line in lines:
        action, n = line[0], int(line[1:])
        match action:
            case "N":
                wx += n
            case "S":
                wx -= n
            case "W":
                wy -= n
            case "E":
                wy += n
            case "L":
                while n:
                    wx, wy = wy, -wx
                    n -= 90
            case "R":
                while n:
                    wx, wy = -wy, wx
                    n -= 90
            case "F":
                x += wx * n
                y += wy * n
    return abs(x) + abs(y)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
