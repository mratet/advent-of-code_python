from aocd import get_data

input = get_data(day=8, year=2018)


def parse_node(data):
    child_count = next(data)
    metadata_count = next(data)
    children = [parse_node(data) for _ in range(child_count)]
    metadata = [next(data) for _ in range(metadata_count)]
    return (children, metadata)


def sum_metadata(node):
    children, metadata = node
    return sum(metadata) + sum(sum_metadata(child) for child in children)


def node_value(node):
    children, metadata = node
    if len(children) == 0:
        return sum_metadata(node)
    return sum(
        node_value(children[metadata_index - 1])
        for metadata_index in metadata
        if metadata_index <= len(children)
    )


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    tree = parse_node(map(int, lines.split()))
    return sum_metadata(tree)


def part_2(lines):
    tree = parse_node(map(int, lines.split()))
    return node_value(tree)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
