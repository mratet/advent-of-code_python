input_rows = open("input.txt").read().splitlines()

NUMBERS = {
    x: i + 1
    for i, x in enumerate(("一", "二", "三", "四", "五", "六", "七", "八", "九", "十"))
} | {  # noqa
    "百": 100,
    "千": 1000,
}

MULTIPLES = {
    "万": 10000,
    "億": 100000000,
}
COMPLETE_DICT = NUMBERS | MULTIPLES

SHAKU = 10 / 33
UNITS = {
    "毛": 1 / 10000,
    "厘": 1 / 1000,
    "分": 1 / 100,
    "寸": 1 / 10,
    "尺": 1,
    "間": 6,
    "丈": 10,
    "町": 360,
    "里": 12960,
}


def parse_japanese_number(value):
    *digits, unit = value
    stack = []
    final_count = 0
    for jap_char in digits:
        if len(stack) == 0:
            stack.append(COMPLETE_DICT[jap_char])
        elif jap_char in MULTIPLES:
            final_count += sum(stack) * MULTIPLES[jap_char]
            stack.clear()
        elif jap_char in NUMBERS:
            curr_value = stack[-1]
            if NUMBERS[jap_char] > curr_value:
                stack[-1] *= NUMBERS[jap_char]
            else:
                stack.append(NUMBERS[jap_char])
    final_count += sum(stack)
    return final_count * UNITS[unit] * SHAKU


total_area = 0
for row in input_rows:
    width, height = map(parse_japanese_number, row.split(" × "))
    total_area += round(width * height)
print(total_area)
