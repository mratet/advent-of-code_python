from bisect import insort

from aocd import get_data

input = get_data(day=9, year=2024)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    disk_map = lines
    compact_disk_map = []
    tot_bytes = 0
    for i, c in enumerate(disk_map):
        n = int(c)
        if i % 2 == 1:
            compact_disk_map.extend(["."] * n)
        else:
            compact_disk_map.extend([str(i // 2)] * n)
            tot_bytes += n

    l = 0
    r = len(compact_disk_map) - 1
    while l < tot_bytes:
        if compact_disk_map[l] != ".":
            l += 1
        else:
            compact_disk_map[l], compact_disk_map[r] = (
                compact_disk_map[r],
                compact_disk_map[l],
            )
            r -= 1
    return sum(i * int(compact_disk_map[i]) for i in range(len(compact_disk_map)) if compact_disk_map[i] != ".")


def part_2(lines):
    disk_map = lines

    files = {}
    free = []
    compact = []
    idx = 0
    for i, c in enumerate(disk_map):
        size, file_id = int(c), i // 2
        if i % 2 == 1:
            compact.extend(["."] * size)
            free.append((idx, size))
        else:
            compact.extend([str(file_id)] * size)
            files[file_id] = (size, idx)
        idx += size

    for file_id, (file_size, file_idx) in reversed(files.items()):
        for free_idx, free_space in free:
            if free_idx > file_idx:
                break
            if file_size <= free_space:
                compact[file_idx : file_idx + file_size] = ["."] * file_size
                compact[free_idx : free_idx + file_size] = [str(file_id)] * file_size
                free.remove((free_idx, free_space))
                if free_space - file_size > 0:
                    insort(free, (free_idx + file_size, free_space - file_size))
                break
    return sum(int(compact[i]) * i for i in range(len(compact)) if compact[i] != ".")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
