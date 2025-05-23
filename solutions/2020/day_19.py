from aocd import get_data, submit

input = get_data(day=19, year=2020)


# WRITE YOUR SOLUTION HERE
def parse_input(data):
    rules_part, messages_part = data.strip().split("\n\n")
    rules = {}
    for line in rules_part.splitlines():
        key, rule = line.split(": ")
        if '"' in rule:
            rules[int(key)] = rule.strip('"')
        else:
            options = rule.split(" | ")
            rules[int(key)] = [list(map(int, option.split())) for option in options]

    return rules, (messages_part.splitlines())


def match_rule(rules, rule_id, input_str, position):
    rule = rules[rule_id]

    if isinstance(rule, str):
        if position < len(input_str) and input_str[position] == rule:
            return [position + 1]
        return []

    possible_positions = []
    for alternative in rule:
        current_positions = [position]
        for part in alternative:
            next_positions = []
            for pos in current_positions:
                next_positions.extend(match_rule(rules, part, input_str, pos))
            current_positions = next_positions
        possible_positions.extend(current_positions)

    return possible_positions


def match(rules, input_str):
    positions = match_rule(rules, 0, input_str, 0)
    return len(input_str) in positions


def part_1(lines):
    rules, messages = parse_input(lines)
    return sum([match(rules, message) for message in messages])


def part_2(lines):
    rules, messages = parse_input(lines)
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    return sum([match(rules, message) for message in messages])


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
