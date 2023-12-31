from aocd import get_data
input = get_data(day=6, year=2015)

import numpy as np

def _parse(line):
     instruction, start, _, end = line.split()[-4:]
     x_min, y_min = list(map(int, start.split(',')))
     x_max, y_max = list(map(int, end.split(',')))
     return instruction, x_min, y_min, x_max, y_max

def part_1(input):
     lights = np.zeros((1000, 1000), dtype=int)

     for line in input.splitlines():
          instruction, x_min, y_min, x_max, y_max = _parse(line)
          match instruction:
               case 'on':
                    lights[x_min:x_max + 1, y_min:y_max + 1] = 1
               case 'off':
                    lights[x_min:x_max + 1, y_min:y_max + 1] = 0
               case 'toggle':
                    lights[x_min:x_max + 1, y_min:y_max + 1] = (lights[x_min:x_max + 1, y_min:y_max + 1] + 1) % 2

     return np.sum(lights)

def part_2(input):
     lights = np.zeros((1000, 1000), dtype=int)

     for line in input.splitlines():
          instruction, x_min, y_min, x_max, y_max = _parse(line)
          match instruction:
               case 'on':
                    lights[x_min:x_max + 1, y_min:y_max + 1] += 1
               case 'off':
                    lights[x_min:x_max + 1, y_min:y_max + 1] -= 1
                    lights[lights < 0] = 0
               case 'toggle':
                    lights[x_min:x_max + 1, y_min:y_max + 1] += 2

     return np.sum(lights)

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
