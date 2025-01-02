from aocd import get_data, submit
input = get_data(day=9, year=2017)

# WRITE YOUR SOLUTION HERE

def stream_processing(stream):
    score = 0
    depth = 0
    garbage_size = 0
    garbage = False
    skip = False

    for char in stream:
        if skip:
            skip = False
            continue

        if char == "!":
            skip = True

        elif garbage:
            if char == ">":
                garbage = False
            else:
                garbage_size += 1
        else:
            if char == "<":
                garbage = True
            elif char == "{":
                depth += 1
                score += depth
            elif char == "}":
                depth -= 1

    return score, garbage_size

def part_1(lines):
    score, _ = stream_processing(lines)
    return score

def part_2(lines):
    _, garbage_size = stream_processing(lines)
    return garbage_size

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
