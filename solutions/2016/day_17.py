from aocd import get_data

input = get_data(day=17, year=2016)

from hashlib import md5

DIRECTIONS = (0, -1, "U"), (0, 1, "D"), (-1, 0, "L"), (1, 0, "R")


def accessible_room(input, current_path):
    code = input + "".join(current_path)
    my_hash = md5(code.encode()).hexdigest()
    state = [c in "bcdef" for c in my_hash[:4]]
    return state


path = []


def find_path(code, current_position, current_path):
    if current_position == (3, 3):
        path.append("".join(current_path))
        return

    acc_room = accessible_room(code, current_path)
    x, y = current_position
    for i, (dx, dy, dir) in enumerate(DIRECTIONS):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4 and acc_room[i]:
            current_path.append(dir)
            find_path(code, (nx, ny), current_path)
            current_path.pop()


def part_1(code):
    find_path(code, (0, 0), [])
    return min(path, key=len)


def part_2(code):
    if not path:
        find_path(code, (0, 0), [])
    return max(map(len, path))


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
