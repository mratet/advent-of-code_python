from aocd import get_data

input = get_data(day=1, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE

word2numbers = {
    "one": "on1e",
    "two": "tw2o",
    "three": "th3ree",
    "four": "fou4r",
    "five": "fi5ve",
    "six": "si6x",
    "seven": "sev7n",
    "eight": "eig8ht",
    "nine": "ni9ne",
}


def solve(line, number_modification):
    if number_modification:
        for word, word_num in word2numbers.items():
            line = line.replace(word, word_num)

    numbers = list(filter(str.isdigit, line))

    return int(numbers[0] + numbers[-1])


def part_1(lines):
    return sum([solve(line, False) for line in lines])


def part_2(lines):
    return sum([solve(line, True) for line in lines])


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
