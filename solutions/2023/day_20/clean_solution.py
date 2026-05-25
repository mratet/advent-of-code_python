import math
from collections import deque

from aocd import get_data

input = get_data(day=20, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE


class Module:
    def __init__(self, name, module_type, outputs):
        self.name = name
        self.type = module_type
        self.outputs = outputs
        self.flip_state = False
        self.memory = {}

    def process(self, origin, pulse, q):
        if self.type == "%":
            if pulse == "lo":
                self.flip_state = not self.flip_state
                outgoing = "hi" if self.flip_state else "lo"
                for output in self.outputs:
                    q.append((self.name, output, outgoing))
        elif self.type == "&":
            self.memory[origin] = pulse
            outgoing = "lo" if all(x == "hi" for x in self.memory.values()) else "hi"
            for output in self.outputs:
                q.append((self.name, output, outgoing))


def parse_input(lines):
    modules = {}
    broadcast_targets = []
    for line in lines:
        source, targets = line.strip().split(" -> ")
        destination_modules = targets.split(", ")
        if source == "broadcaster":
            broadcast_targets = destination_modules
        else:
            module_type, module_name = source[0], source[1:]
            modules[module_name] = Module(module_name, module_type, destination_modules)
    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "lo"
    return broadcast_targets, modules


def part_1(lines):
    # Solution taken from hyper-neutrino
    broadcast, modules = parse_input(lines)
    lo = hi = 0
    for _ in range(1000):
        lo += 1
        q = deque([("broadcaster", x, "lo") for x in broadcast])
        while q:
            origin, target, pulse = q.popleft()
            if pulse == "lo":
                lo += 1
            else:
                hi += 1
            if target in modules:
                modules[target].process(origin, pulse, q)
    return lo * hi


def part_2(lines):
    # Solution taken from hyper-neutrino
    # You need to explore the graph to understand the solution
    # well explained there at 1:15:00 https://www.youtube.com/watch?v=C5wYxR6ZAPM
    broadcast, modules = parse_input(lines)
    (feed,) = [name for name, module in modules.items() if "rx" in module.outputs]
    cycle_lengths = {}
    seen = {name: 0 for name, module in modules.items() if feed in module.outputs}
    presses = 0
    while True:
        presses += 1
        q = deque([("broadcaster", x, "lo") for x in broadcast])
        while q:
            origin, target, pulse = q.popleft()
            if target not in modules:
                continue
            if target == feed and pulse == "hi":
                seen[origin] += 1
                if origin not in cycle_lengths:
                    cycle_lengths[origin] = presses
                if all(seen.values()):
                    return math.lcm(*cycle_lengths.values())
            modules[target].process(origin, pulse, q)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
