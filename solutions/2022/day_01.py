from aocd import get_data

input = get_data(day=1, year=2022).split("\n\n")


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    carried_calories = [sum(int(cal) for cal in elf.splitlines()) for elf in lines]
    return max(carried_calories)


def part_2(lines):
    carried_calories = [sum(int(cal) for cal in elf.splitlines()) for elf in lines]
    carried_calories.sort(reverse=True)
    return sum(carried_calories[:3])


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
