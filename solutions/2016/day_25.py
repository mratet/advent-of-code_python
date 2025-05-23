from aocd import get_data

input = get_data(day=25, year=2016).splitlines()


def program_execution(registers, input):
    line_index = 0
    n = len(input)
    sig = []

    while line_index < n and len(sig) < 15:
        instructions, *args = input[line_index].split()
        match instructions:
            case "inc":
                c = args[0]
                registers[c] = registers[c] + 1
            case "dec":
                c = args[0]
                registers[c] = registers[c] - 1
            case "out":
                c = args[0]
                value = registers[c] if c in "abcd" else int(c)
                sig.append(value)
            case "cpy":
                x, y = args[0], args[1]
                if y.isdigit():
                    continue
                registers[y] = registers[x] if x in "abcd" else int(x)
            case "jnz":
                x, y = args[0], args[1]
                cond = registers[x] if x in "abcd" else int(x)
                cond2 = registers[y] if y in "abcd" else int(y)
                line_index += cond2 if cond != 0 else 1
                line_index -= 1
            case "tgl":
                x = args[0]
                cond = registers[x] if x in "abcd" else int(x)
                if 0 <= line_index + cond < n - 1:
                    line = input[line_index + cond].split()
                    match line[0]:
                        case "inc":
                            input[line_index + cond] = input[line_index + cond].replace(
                                "inc", "dec"
                            )
                        case "dec":
                            input[line_index + cond] = input[line_index + cond].replace(
                                "dec", "inc"
                            )
                        case "tgl":
                            input[line_index + cond] = input[line_index + cond].replace(
                                "tgl", "inc"
                            )
                        case "jnz":
                            input[line_index + cond] = input[line_index + cond].replace(
                                "jnz", "cpy"
                            )
                        case "cpy":
                            input[line_index + cond] = input[line_index + cond].replace(
                                "cpy", "jnz"
                            )
        line_index += 1

    return registers, sig


def part_1(input):
    # The program will print the inverse binary representation of N - b * c
    binary = "010101010101"
    return int(binary[::-1], 2) - 4 * 643


print(f"My answer is {part_1(input)}")
