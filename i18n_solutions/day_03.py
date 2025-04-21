input_rows = open("input.txt").read().splitlines()

valid_passwords = 0
for password in input_rows:
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_non_ascii = any(ord(c) > 127 for c in password)
    if (
        4 <= len(password) <= 12
        and has_digit
        and has_upper
        and has_lower
        and has_non_ascii
    ):
        valid_passwords += 1
print(valid_passwords)
