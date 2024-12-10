from aocd import get_data, submit
input = get_data(day=9, year=2024)
import bisect

# WRITE YOUR SOLUTION HERE
def part_1(lines):
    disk_map = lines
    compact_disk_map = []
    tot_bytes = 0
    for i, c in enumerate(disk_map):
        if i % 2 == 1:
            compact_disk_map.extend(['.'] * int(c))
        else :
            compact_disk_map.extend([str(i // 2)] * int(c))
            tot_bytes += int(c)

    r = len(compact_disk_map) - 1
    l = 0
    while l < tot_bytes:
        if compact_disk_map[l] != '.':
            l += 1
        else:
            compact_disk_map[l], compact_disk_map[r] = compact_disk_map[r], compact_disk_map[l]
            r -= 1
    return sum([i * int(compact_disk_map[i]) for i in range(len(compact_disk_map)) if compact_disk_map[i] != '.'])

def part_2(lines):
    disk_map = lines

    files = {}
    free = []
    compact = []
    idx = 0
    for i, c in enumerate(disk_map):
        C, file_id = int(c), i // 2
        if i % 2 == 1:
            compact.extend(['.'] * C)
            free.append((idx, C))
        else :
            compact.extend([str(file_id)] * C)
            files[file_id] = (C, idx)
        idx += C

    free.sort()

    for file_id, (file_size, file_idx) in reversed(files.items()):
        for (free_idx, free_space) in free:
            if free_idx > file_idx: break
            if file_size <= free_space:
                compact[file_idx : file_idx + file_size] = ['.'] * file_size
                compact[free_idx : free_idx + file_size] = [str(file_id)] * file_size
                free.remove((free_idx, free_space))
                if free_space - file_size > 0:
                    bisect.insort(free, (free_idx + file_size, free_space - file_size))
                break
    return sum([int(compact[i]) * i for i in range(len(compact)) if compact[i] != '.'])

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
