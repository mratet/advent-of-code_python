import itertools

from functools import cache

import unicodedata
import bcrypt


input_blocks = open("input.txt").read().split("\n\n")


@cache
def bcrypt_check(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


def generate_unicode_variants(chars):
    char_variants = [{char, unicodedata.normalize("NFD", char)} for char in chars]
    for variant_combination in itertools.product(*char_variants):
        yield "".join(variant_combination)


authentication_database, login_attempts = input_blocks
authentification = {}
for row in authentication_database.splitlines():
    username, bcrypted_password = row.split()
    authentification[username] = bcrypted_password

valid_logins = 0
for row in login_attempts.splitlines():
    username, attempt_password = row.split()
    norm_password = unicodedata.normalize("NFC", attempt_password)
    if any(
        bcrypt_check(possible_password, authentification[username])
        for possible_password in generate_unicode_variants(norm_password)
    ):
        valid_logins += 1
print(valid_logins)
