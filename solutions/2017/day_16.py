from aocd import get_data, submit

input = get_data(day=16, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    programs = [ord("a") + i for i in range(16)]
    instruc = lines[0].split(",")
    programs = dance(programs, instruc)
    return "".join([chr(s) for s in programs])


def dance(programs, instruc):
    for inst in instruc:
        if inst[0] == "x":
            A, B = map(int, inst[1:].split("/"))
            programs[A], programs[B] = programs[B], programs[A]
        elif inst[0] == "p":
            A, B = inst[1:].split("/")
            idx1, idx2 = programs.index(ord(A)), programs.index(ord(B))
            programs[idx1], programs[idx2] = programs[idx2], programs[idx1]
        elif inst[0] == "s":
            idx = 16 - int(inst[1:])
            programs = programs[idx:] + programs[:idx]
    return programs


def part_2(lines):
    programs = [ord("a") + i for i in range(16)]
    instruc = lines[0].split(",")
    S = set()
    N = 0
    while tuple(programs) not in S:
        S.add(tuple(programs))
        programs = dance(programs, instruc)
        N += 1

    # It happens to be a perfect cycle so a modulo is enough
    for _ in range(100000000 % N):
        programs = dance(programs, instruc)
    return "".join([chr(s) for s in programs])


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
