input_rows = open("input.txt").read().splitlines()

height, max_width = len(input_rows), max(len(row) for row in input_rows)
print(
    sum(
        row[idx] == "💩"
        for i, row in enumerate(input_rows)
        if (idx := (2 * i) % max_width) < len(row)
    )
)
