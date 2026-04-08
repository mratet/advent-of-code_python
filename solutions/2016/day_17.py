from hashlib import md5

from aocd import get_data

input = get_data(day=17, year=2016)

DIRECTIONS = (0, -1, "U"), (0, 1, "D"), (-1, 0, "L"), (1, 0, "R")


def get_open_doors(code, current_path):
    my_hash = md5((code + current_path).encode()).hexdigest()
    return [c in "bcdef" for c in my_hash[:4]]


def find_all_paths(passcode):
    paths = []

    def dfs(x, y, path):
        if (x, y) == (3, 3):
            paths.append(path)
            return

        open_doors = get_open_doors(passcode, path)
        for i, (dx, dy, dir) in enumerate(DIRECTIONS):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4 and open_doors[i]:
                dfs(nx, ny, path + dir)

    dfs(0, 0, "")
    return paths


def part_1(input):
    return min(find_all_paths(input), key=len)


def part_2(input):
    return max(map(len, find_all_paths(input)))


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
