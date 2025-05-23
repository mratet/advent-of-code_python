
# input = get_data(day=1, year=2024).splitlines()
import re

input = open(0).read()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return


def part_2(lines):
    return


# END OF SOLUTION
# print(f'My answer is {part_1(input)}')
# print(f'My answer is {part_2(input)}')


def parse_test_input(input):
    examples = re.findall(
        r"Example data \d+/\d+ --+\n(.*?)\n-+\nanswer_a: (\d+)\nanswer_b: ([^\n]+)",
        input,
        re.DOTALL,
    )

    results = []
    for example_text, answer_a, answer_b in examples:
        # Clean up the example text, remove trailing and leading empty lines
        example_lines = example_text.strip().splitlines()
        results.append(
            {"example": example_lines, "answer_a": int(answer_a), "answer_b": answer_b}
        )
    return results


if input[190:206] == "--- Example data":
    results = parse_test_input(input)
    for i, result in enumerate(results):
        test_input, answer_a, answer_b = result.values()
        print(f"{i + 1} : My test answer is {part_1(test_input)} vs {answer_a}")
        print(f"My test answer is {part_2(test_input)} vs {answer_b}")
else:
    input = input.splitlines()
    print(f"My answer is {part_1(input)}")
    print(f"My answer is {part_2(input)}")
    # submit(part_1(input), part="a", day=1, year=2024)
    # submit(part_2(input), part="b", day=1, year=2024)
