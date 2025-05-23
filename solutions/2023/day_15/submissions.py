import collections

lines = open("input.txt").read().splitlines()

# WRITE YOUR SOLUTION HERE


def hash(string):
    value = 0
    for c in string:
        value = ((value + ord(c)) * 17) % 256
    return value


def part_1(lines):
    sequence = lines[0].split(",")
    ans = 0
    for u in sequence:
        ans += hash(u)
    return ans


def part_2(lines):
    sequence = lines[0].split(",")
    boxes = collections.defaultdict(list)
    for u in sequence:
        if "-" in u:
            label = u[:-1]
            box_number = hash(label)

            for i, (lab, _) in enumerate(boxes[box_number]):
                if lab == label:
                    boxes[box_number].pop(i)
        else:
            label, focal_length = u.split("=")
            box_number = int(hash(label))
            index = [i for i, (lab, _) in enumerate(boxes[box_number]) if label == lab]
            if index:
                boxes[box_number][index[0]] = (label, int(focal_length))
            else:
                boxes[box_number].append((label, int(focal_length)))

    ans = 0
    for box_number in boxes.keys():
        for i, (l, focal_length) in enumerate(boxes[box_number]):
            ans += (box_number + 1) * (i + 1) * focal_length
    return ans


# END OF SOLUTION


test_input = open("input-test.txt").read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == "-":
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f"My answer on test set for the first problem is {part_1(test_lines)}")
print(solution)
print(f"My answer is {part_1(lines)}")

print(f"My answer on test set for the second problem is {part_2(test_lines)}")
print(f"My answer is {part_2(lines)}")
