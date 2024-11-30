from aocd import get_data
input = get_data(day=23, year=2020)

# WRITE YOUR SOLUTION HERE
def get_next_turn(state, starting_pos):
    N = len(state)
    pu_cups = [state[(starting_pos + i) % N] for i in range(1, 4)]
    current_cup = state[starting_pos]

    for i in range(1, 5):
        elt = (state[starting_pos] - i - 1) % N + 1
        if elt not in pu_cups:
            destination_cup = elt
            break

    state = state[:]
    for cup in pu_cups:
        state.remove(cup)
    idx = state.index(destination_cup)
    for i in range(1, 4):
        state.insert((idx + i) % N, pu_cups[i - 1])

    return state, (state.index(current_cup) + 1) % N

def get_state_slow_ver(state, N):
    current_pos = 0
    for i in range(N):
        state, current_pos = get_next_turn(state, current_pos)
    idx = state.index(1)
    return ''.join([str(n) for n in (state[1 + idx:] + state[:idx])])

def part_1(lines):
    init_state = [int(n) for n in lines]
    return get_state_slow_ver(init_state, 100)

def next_turn(next, current_cup):
    N = len(next) - 1
    destination_cup = None

    n1 = next[current_cup]
    n2 = next[n1]
    n3 = next[n2]
    pu_cups = {n1, n2, n3}

    for i in range(1, 5):
        elt = (current_cup - i - 1) % N + 1
        if elt not in pu_cups:
            destination_cup = elt
            break

    destination_cup_neigh = next[destination_cup]
    next[current_cup] = next[n3]
    next[destination_cup] = n1
    next[n3] = destination_cup_neigh

    return next, next[current_cup]

def get_state_fast_ver(init_state, N):
    current_cup = init_state[0]
    state = [0] * len(init_state)
    for (i, j) in zip(init_state, init_state[1:]):
        state[i] = j

    for _ in range(N):
        state, current_cup = next_turn(state, current_cup)
    return state

def part_2(lines):
    state_size = 1000000 + 1
    init_state = [int(n) for n in lines] + list(range(10, state_size))
    init_state.append(init_state[0])

    state = get_state_fast_ver(init_state, 10000000)
    return state[1] * state[state[1]]

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')

