from aocd import get_data, submit

input = get_data(day=11, year=2017)


# WRITE YOUR SOLUTION HERE
def get_dist_array(dirs):
    x, y = 0, 0
    dist = []
    for d in dirs:
        if d == "n":
            x += 2
        elif d == "s":
            x -= 2
        elif d == "ne":
            x += 1
            y += 1
        elif d == "sw":
            x -= 1
            y -= 1
        elif d == "nw":
            x += 1
            y -= 1
        elif d == "se":
            x -= 1
            y += 1
        dist.append((abs(x) + abs(y)) // 2)
    return dist


def part_1(lines):
    inst = [n for n in lines.split(",")]
    dist_array = get_dist_array(inst)
    return dist_array[-1]


def part_2(lines):
    inst = [n for n in lines.split(",")]
    dist_array = get_dist_array(inst)
    return max(dist_array)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
