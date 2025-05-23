from aocd import get_data

input = get_data(day=15, year=2016).splitlines()


def _parse(input):
    disks = []
    for line in input:
        line = line.split()
        disks.append([int(line[3]), int(line[-1][:-1])])
    return disks


def find_perfect_button_push(disks):
    # N + i + 1 + start % length == 0
    # N % length == -(i + 1 + start) % length
    # Possible to design a solution using Chinese Reminder Theorem for fast inference
    n = 0
    while not all(
        [(n + i + 1 + start) % length == 0 for i, (length, start) in enumerate(disks)]
    ):
        n += 1
    return n


def part_1(input):
    disks = _parse(input)
    return find_perfect_button_push(disks)


def part_2(input):
    disks = _parse(input)
    disks.append([11, 0])
    return find_perfect_button_push(disks)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
