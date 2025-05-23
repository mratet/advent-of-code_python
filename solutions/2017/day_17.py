from aocd import get_data, submit

input = get_data(day=17, year=2017)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    N = int(lines)
    tab = [0]
    idx = 0
    for i in range(1, 2018):
        idx = (idx + N) % len(tab) + 1
        tab.insert(idx, i)
    return tab[tab.index(2017) + 1]


def part_2(lines):
    N = int(lines)
    idx = 0
    val = 0
    for i in range(1, 50000001):
        idx = (idx + N) % i + 1
        if idx == 1:
            val = i
    return val


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
