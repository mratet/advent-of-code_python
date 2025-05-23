import collections

from aocd import get_data

input = get_data(day=2, year=2023).splitlines()


# WRITE YOUR SOLUTION HERE
def _parse(line):
    games = line.split(":")[1].split(";")
    synthesis = collections.defaultdict(list)

    for game_set in games:
        game = game_set.split(",")
        for tirage in game:
            tirage = tirage.split(" ")
            number, color = tirage[1], tirage[2]
            synthesis[color].append(int(number))

    return synthesis


def part_1(input):
    max_values = {"red": 12, "green": 13, "blue": 14}

    ans = 0
    for i, line in enumerate(input):
        synthesis = _parse(line)
        if all(
            [
                all([max_val >= val for val in synthesis[k]])
                for k, max_val in max_values.items()
            ]
        ):
            ans += i + 1

    return ans


def part_2(input):
    ans = 0
    for i, line in enumerate(input):
        synthesis = _parse(line)
        b, g, r = [max(color_val) for k, color_val in synthesis.items()]
        ans += b * g * r

    return ans


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
