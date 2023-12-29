from aocd import get_data
input = get_data(day=20, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
import math
from collections import deque

class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == '%':
            self.memory = 'off'
        else:
            self.memory = {}

    def __repr__(self):
        return self.name + "{type=" + self.type + ",outputs=" + ",".join(self.outputs) + ",memory=" + str(self.memory) + "}"

def _parse(lines):
    modules = {}
    broadcasts_targets = []

    for line in lines:
        l, r = line.strip().split(' -> ')
        destination_modules = r.split(', ')
        if l == 'broadcaster':
            broadcasts_targets = destination_modules
        else:
            module_type = l[0]
            module_name = l[1:]
            modules[module_name] = Module(module_name, module_type, destination_modules)

    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == '&':
                modules[output].memory[name] = 'lo'

    return broadcasts_targets, modules


def part_1(input):
    # Solution taken from hyper-neutrino
    broadcast, modules = _parse(input)

    lo = hi = 0
    for _ in range(1000):
        lo += 1
        q = deque([('broadcaster', x, 'lo') for x in broadcast])

        while q:
            origin, target, pulse = q.popleft()

            if pulse == 'lo':
                lo += 1
            else:
                hi += 1

            if target not in modules:
                continue

            module = modules[target]
            if module.type == "%":
                if pulse == "lo":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "hi" if module.memory == "on" else "lo"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))

    return lo * hi


def part_2(input):
    # Solution taken from hyper-neutrino
    # You need to explore the graph to understand the solution
    # weel explainded there at 1:15:00 https://www.youtube.com/watch?v=C5wYxR6ZAPM
    broadcast, modules = _parse(input)

    (feed,) = [name for name, module in modules.items() if 'rx' in module.outputs]

    cycle_lenghts = {}
    seen = {name: 0 for name, module in modules.items() if feed in module.outputs}

    presses = 0

    while True:
        presses += 1
        q = deque([('broadcaster', x, 'lo') for x in broadcast])
        while q:
            origin, target, pulse = q.popleft()

            if target not in modules:
                continue

            module = modules[target]

            if module.name == feed and pulse == 'hi':
                seen[origin] += 1
                if origin not in cycle_lenghts:
                    cycle_lenghts[origin] = presses
                else:
                    assert presses == seen[origin] * cycle_lenghts[origin]

                if all(seen.values()):
                    print(math.lcm(*cycle_lenghts.values()))
                    exit()

            if module.type == "%":
                if pulse == "lo":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "hi" if module.memory == "on" else "lo"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
# END OF SOLUTION


print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
