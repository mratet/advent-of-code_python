input_rows = open("input.txt").read().splitlines()

bill = 0
for message in input_rows:
    bytes_count, char_count = len(message.encode("utf-8")), len(message)
    if bytes_count <= 160 and char_count <= 140:
        bill += 13
    elif char_count <= 140:
        bill += 7
    elif bytes_count <= 160:
        bill += 11

print(bill)
