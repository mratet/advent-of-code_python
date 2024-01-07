from aocd import get_data
input = get_data(day=6, year=2015)

import numpy as np
import re

def _parse(line):
     op, x_min, y_min, x_max, y_max = re.search('(\w+) (\d+),(\d+) through (\d+),(\d+)', line).groups()
     return op, int(x_min), int(y_min), int(x_max) + 1, int(y_max) + 1

def part_1(input):
     lights = np.zeros((1000, 1000), dtype=int)

     for line in input.splitlines():
          instruction, x_min, y_min, x_max, y_max = _parse(line)
          match instruction:
               case 'on':
                    lights[x_min:x_max, y_min:y_max] = 1
               case 'off':
                    lights[x_min:x_max, y_min:y_max] = 0
               case 'toggle':
                    lights[x_min:x_max, y_min:y_max] = 1 - lights[x_min:x_max, y_min:y_max]

     return np.sum(lights)

def part_2(input):
     lights = np.zeros((1000, 1000), dtype=int)

     for line in input.splitlines():
          instruction, x_min, y_min, x_max, y_max = _parse(line)
          match instruction:
               case 'on':
                    lights[x_min:x_max, y_min:y_max] += 1
               case 'off':
                    lights[x_min:x_max, y_min:y_max] -= 1
                    lights[lights < 0] = 0
               case 'toggle':
                    lights[x_min:x_max, y_min:y_max] += 2

     return np.sum(lights)

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
