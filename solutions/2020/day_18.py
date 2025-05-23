from aocd import get_data

input = get_data(day=18, year=2020).splitlines()


# WRITE YOUR SOLUTION HERE
def evaluate(input):
    ram = {}
    letter = 65

    def pure_evaluation(data):
        cnt = int(data[0]) if data[0].isdigit() else ram[data[0]]
        for exp, n in zip(data[1::2], data[2::2]):
            val = int(n) if n.isdigit() else ram[n]
            if exp == "+":
                cnt += val
            elif exp == "*":
                cnt *= val
        return cnt

    while True:
        idx = input.find(")")
        if idx == -1:
            return pure_evaluation(input)
        open = idx - 1
        while input[open] != "(":
            open -= 1
        ram[chr(letter)] = pure_evaluation(input[open + 1 : idx])
        input = input.replace(input[open : idx + 1], chr(letter), 1)
        letter += 1


def part_1(lines):
    return sum([evaluate(line.replace(" ", "")) for line in lines])


def add_parentheses_around_plus(line):
    text = list(line)
    while "+" in text:
        idx = text.index("+")
        text[idx] = "."  # momentany replacement
        if text[idx - 1].isdigit():
            text.insert(idx - 1, "(")
        elif text[idx - 1] == ")":
            cnt_parenthesis = 1
            left_idx = idx - 1
            while cnt_parenthesis:
                left_idx -= 1
                if text[left_idx] == "(":
                    cnt_parenthesis -= 1
                elif text[left_idx] == ")":
                    cnt_parenthesis += 1
            text.insert(left_idx, "(")

        idx += 1  # Add a symbol on the left part
        if text[idx + 1].isdigit():
            text.insert(idx + 2, ")")
        elif text[idx + 1] == "(":
            cnt_parenthesis = 1
            right_idx = idx + 1
            while cnt_parenthesis:
                right_idx += 1
                if text[right_idx] == ")":
                    cnt_parenthesis -= 1
                if text[right_idx] == "(":
                    cnt_parenthesis += 1
            text.insert(right_idx, ")")

    return "".join(text).replace(".", "+")


def part_2(lines):
    return sum(
        [evaluate(add_parentheses_around_plus(line.replace(" ", ""))) for line in lines]
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
