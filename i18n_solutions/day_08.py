from collections import Counter
from string import ascii_lowercase
import unicodedata


input_rows = open("input.txt").read().splitlines()

VOWELS = "aeiou"
CONSONANTS = set(ascii_lowercase) - set(VOWELS)


valid_passwords = 0
for password in input_rows:
    normalized_password = unicodedata.normalize("NFD", password).casefold()
    has_digit = any(w.isdigit() for w in password)
    has_vowel = any(v in normalized_password for v in VOWELS)
    has_consonant = any(c in normalized_password for c in CONSONANTS)
    letter_counter = Counter(normalized_password)
    no_recurring = all([letter_counter[letter] < 2 for letter in ascii_lowercase])
    if (
        4 <= len(password) <= 12
        and has_digit
        and has_vowel
        and has_consonant
        and no_recurring
    ):
        valid_passwords += 1
print(valid_passwords)
