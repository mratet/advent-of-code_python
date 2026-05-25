from aocd import get_data

input = get_data(day=9, year=2020).splitlines()


# WRITE YOUR SOLUTION HERE
def two_sum(num_list, numb):
    seen = set()
    for n in num_list:
        if numb - n in seen:
            return True
        seen.add(n)
    return False


def part_1(lines):
    lines = [int(n) for n in lines]
    step = 25
    for i in range(step, len(lines)):
        window, target = lines[i - step : i], lines[i]
        if not two_sum(window, target):
            return target


def part_2(lines):
    N = part_1(lines)
    lines = [int(n) for n in lines]
    left, right, s = 0, 1, lines[0]
    while s != N:
        if s > N:
            s -= lines[left]
            left += 1
        else:
            s += lines[right]
            right += 1
    return min(lines[left:right]) + max(lines[left:right])


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
