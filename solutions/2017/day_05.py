from aocd import get_data, submit

input = get_data(day=5, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    i = 0
    inst = [int(n) for n in lines]
    count = 0
    while i < len(inst):
        inst[i] += 1
        i += inst[i] - 1
        count += 1
    return count


def part_2(lines):
    i = 0
    inst = [int(n) for n in lines]
    count = 0
    while i < len(inst):
        current_pos = i
        i += inst[i]
        if inst[current_pos] < 3:
            inst[current_pos] += 1
        else:
            inst[current_pos] -= 1
        count += 1
    return count


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
