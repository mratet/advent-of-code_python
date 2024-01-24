import itertools, re, collections, functools
from aocd import get_data
input = get_data(day=11, year=2016).splitlines()


'''
The parsing is good but the batracking part as to be corrected !!
'''

def _parse_input(input):
    state = [[] for _ in range(4)]
    for i, line in enumerate(input):
        line = line.replace('and', '')
        line = line.replace('-compatible', ' ')
        line = line.split(' a ')
        state[i].append('empty')
        for word in line[1:]:
            c = ''
            for w in word.split():
                c += w[0].upper()
                if len(c) == 1:
                    c += w[1]
            state[i].append(c)
    return state


def verify_explosion(stage):
    for floor in stage:
        for module in floor:
            if module[-1] == 'M' and module[:2] + 'G' not in floor:
                if any([mod[-1] == 'G' for mod in floor]):
                    return False
    return True

def encode_state(state):
    c = ''
    for i, floor in enumerate(state):
        floor = sorted(floor)
        c += str(i) + str(floor)
    return c


def solve(state, elevator_pos, cnt):
    if len(state[0]) + len(state[1]) + len(state[3]) == 3:
        return

    # if cnt > 100:
    #     return

    if encode_state(state) in states:
        return
    else:
        states.add(encode_state(state))
        # print(encode_state(state))

    if not verify_explosion(state):
        return


    l_floor, u_floor = max(elevator_pos - 1, 0), min(elevator_pos + 1, 3)
    for modules, floor in itertools.product(itertools.product(state[elevator_pos], state[elevator_pos]), (l_floor, u_floor)):
        if modules[0] == modules[1]: continue
        if floor == elevator_pos:
            continue

        for m in modules:
            if m == 'empty': continue
            state[elevator_pos].remove(m)
            state[floor].append(m)

        solve(state, floor, cnt + 1)

        for m in modules:
            if m == 'empty': continue
            state[floor].remove(m)
            state[elevator_pos].append(m)


starting_state = _parse_input(input)
states = set()
print(solve(starting_state, 0, 0))




# print(f'My answer is {part_1(input)}')
# print(f'My answer is {part_2(input)}')
