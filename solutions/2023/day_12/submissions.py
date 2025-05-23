from functools import cache

lines = open("input.txt").read().splitlines()

# WRITE YOUR SOLUTION HERE


def generate_all_sequences(n, decoded_list):
    if len(decoded_list) == 1:
        length = decoded_list[0]
        all_tab = []
        for i in range(n - length + 1):
            tab = ["."] * n
            tab[i : i + length] = "#" * length
            all_tab.append(tab)
        return all_tab

    last_pos = n - sum(decoded_list) - len(decoded_list) + 2
    first_len = decoded_list.pop(0)
    all_tab = []
    for start_pos in range(last_pos):
        tab = ["."] * (start_pos + first_len + 1)
        tab[start_pos : start_pos + first_len] = "#" * first_len
        next_tab = generate_all_sequences(
            n - start_pos - first_len - 1, decoded_list.copy()
        )
        for x in next_tab:
            all_tab.append(tab + x)
    return all_tab


def check_sequence(damaged_strings, all_strings):
    cnt = 0
    flag = True
    for string in all_strings:
        for i, c in enumerate(string):
            if damaged_strings[i] != "?" and damaged_strings[i] != c:
                flag = False
        if flag:
            cnt += 1
        flag = True

    return cnt


def part_1(lines):
    l = 0
    for line in lines:
        encoded, decoded = line.split()
        # encoded = [c for c in encoded.split('.') if c != '']
        decoded = [int(c) for c in decoded.split(",")]
        all_seq = generate_all_sequences(len(encoded), decoded)
        l += check_sequence(encoded, all_seq)

    return l


@cache
def solve(string, decoded):
    # Solution from HyperNeutrino
    if string == "":
        return 1 if decoded == () else 0
    if decoded == ():
        return 0 if "#" in string else 1

    result = 0

    if string[0] in ".?":
        result += solve(string[1:], decoded)

    if string[0] in "#?":
        current_len = decoded[0]
        if (
            current_len <= len(string)
            and "." not in string[:current_len]
            and (current_len == len(string) or string[current_len] != "#")
        ):
            result += solve(string[current_len + 1 :], decoded[1:])

    return result


def part_2(lines):
    ans = 0
    for i, line in enumerate(lines):
        encoded, decoded = line.split()
        decoded = tuple([int(c) for c in decoded.split(",")])
        encoded = ((encoded + "?") * 5)[:-1]
        decoded = decoded * 5
        ans += solve(encoded, decoded)
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
