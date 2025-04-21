import math


from unidecode import unidecode
import unicodedata


input_rows = open("input.txt").read().splitlines()


def english_key(name):
    return unidecode(name).casefold()


def get_sorted_key(replace_dict, name):
    name = unicodedata.normalize("NFD", name)
    name = name.casefold()
    for k, v in replace_dict.items():
        k = unicodedata.normalize("NFD", k)
        name = name.replace(k, v)
    name = "".join([x for x in name if x.isalpha() or x == ","])
    return name


def swedish_key(name):
    swedish_dict = {"ø": "ö", "æ": "å", "ä": "å", "å": "ä", "ö": "ö"}
    return get_sorted_key(swedish_dict, name)


def dutch_key(name):
    dutch_dict = {
        "ø": "o",
        "æ": "ae",
        "ı": "i",
        "van den": "",
        "van der": "",
        "van ": "",
        "de ": "",
    }
    return get_sorted_key(dutch_dict, name)


def get_middle_number(key):
    s = sorted(input_rows, key=key)
    return int(s[len(s) // 2].split(": ")[-1])


print(math.prod(get_middle_number(fn) for fn in (english_key, swedish_key, dutch_key)))
