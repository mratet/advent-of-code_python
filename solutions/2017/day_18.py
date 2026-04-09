from collections import defaultdict

from aocd import get_data

input = get_data(day=18, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def program_execution(program, state, part="part_2"):
    pos = state["pos"]
    registers = state["registers"]
    snd_queue = state["snd_queue"]
    rcv_queue = state["rcv_queue"]
    cnt = state["count"]
    get_value = lambda v: int(v) if v.lstrip("-").isdigit() else registers[v]

    while pos < len(program):
        op, *args = program[pos].split()

        if op == "snd":
            cnt += 1
            snd_queue.append(get_value(args[0]))
        elif op == "set":
            registers[args[0]] = get_value(args[1])
        elif op == "add":
            registers[args[0]] += get_value(args[1])
        elif op == "mul":
            registers[args[0]] *= get_value(args[1])
        elif op == "mod":
            registers[args[0]] %= get_value(args[1])
        elif op == "rcv":
            if part == "part_1" and get_value(args[0]) != 0:
                state.update(pos=pos, count=cnt)
                return state
            else:
                if not rcv_queue:
                    state.update(pos=pos, count=cnt)
                    return state
                registers[args[0]] = rcv_queue.pop(0)
        elif op == "jgz":
            if get_value(args[0]) > 0:
                pos += get_value(args[1]) - 1
        pos += 1


def part_1(lines):
    state = {"pos": 0, "registers": defaultdict(int), "snd_queue": [], "rcv_queue": [], "count": 0}
    state = program_execution(lines, state, part="part_1")
    return state["snd_queue"][-1]


def part_2(lines):
    state0 = {
        "pos": 0,
        "registers": defaultdict(int),
        "snd_queue": [],
        "rcv_queue": [],
        "count": 0,
    }
    state1 = {
        "pos": 0,
        "registers": defaultdict(int),
        "snd_queue": [],
        "rcv_queue": [],
        "count": 0,
    }
    state1["registers"]["p"] = 1
    while True:
        state0 = program_execution(lines, state0)
        state1 = program_execution(lines, state1)
        snd_q0, snd_q1 = state0["snd_queue"], state1["snd_queue"]
        if not snd_q0 and not snd_q1:
            break
        state0["rcv_queue"].extend(snd_q1)
        state1["rcv_queue"].extend(snd_q0)
        state0["snd_queue"], state1["snd_queue"] = [], []
    return state1["count"]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
