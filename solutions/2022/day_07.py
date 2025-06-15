from dataclasses import dataclass

from aocd import get_data

input = get_data(day=7, year=2022).splitlines()


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children_dirs = []
        self.children_files = []


@dataclass
class File:
    name: str
    size: int


def parse_filesystem(lines):
    root = Dir("/")
    current = root
    all_dirs = [root]
    i = 0

    while i < len(lines):
        line = lines[i]
        if line.startswith("$"):
            cmd_parts = line[2:].split()
            cmd = cmd_parts[0]

            if cmd == "ls":
                i += 1
                while i < len(lines) and not lines[i].startswith("$"):
                    item = lines[i].split()
                    if item[0].isdigit():
                        size = int(item[0])
                        name = item[1]
                        if not any(f.name == name for f in current.children_files):
                            current.children_files.append(File(name, size))
                    else:
                        name = item[1]
                        if not any(d.name == name for d in current.children_dirs):
                            new_dir = Dir(name, parent=current)
                            current.children_dirs.append(new_dir)
                            all_dirs.append(new_dir)
                    i += 1
                continue  # skip the i += 1 below, already moved
            elif cmd == "cd":
                target = cmd_parts[1]
                if target == "/":
                    current = root
                elif target == "..":
                    current = current.parent if current.parent else current
                else:
                    current = next(d for d in current.children_dirs if d.name == target)
        i += 1

    return root, all_dirs


def compute_directory_size(directory):
    size = sum(f.size for f in directory.children_files)
    for sub_dir in directory.children_dirs:
        size += compute_directory_size(sub_dir)
    return size


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    _, all_dirs = parse_filesystem(lines)
    return sum(size for d in all_dirs if (size := compute_directory_size(d)) <= 100_000)


def part_2(lines):
    root_dir, all_dirs = parse_filesystem(lines)
    TOTAL_SPACE = 70_000_000
    NEEDED_SPACE = 30_000_000
    used_space = compute_directory_size(root_dir)
    free_space = TOTAL_SPACE - used_space
    missing_space = NEEDED_SPACE - free_space

    valid_dirs = [d for d in all_dirs if compute_directory_size(d) >= missing_space]
    smallest = min(valid_dirs, key=compute_directory_size)

    return compute_directory_size(smallest)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
