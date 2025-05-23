from aocd import get_data

input = get_data(day=9, year=2020).splitlines()


# WRITE YOUR SOLUTION HERE
def two_sum(num_list, numb):
    seen = set()
    for n in num_list:
        if numb - n in seen:
            return True
        seen.add(n)


def part_1(lines):
    lines = [int(n) for n in lines]
    step = 25
    for i in range(step, len(lines)):
        num_list, numb = lines[i - step : i], lines[i]
        if not (two_sum(num_list, numb)):
            return numb


def part_2(lines):
    lines = [int(n) for n in lines]
    N = part_1(lines)
    l, r, s = 0, 1, 0
    while s != N:
        s = sum(lines[l:r])
        if s > N:
            l += 1
        elif s < N:
            r += 1
    return min(lines[l:r]) + max(lines[l:r])


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
