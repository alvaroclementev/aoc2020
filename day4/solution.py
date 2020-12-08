"""
Solutions to Day 4 of Advent of Code by Alvaro Clemente
"""
import re
from functools import partial

REQUIRED = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

HAIR_COLORS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def parse_input(filename):
    """
    Parse the input files into passports
    E.g:
        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929

    A passport has key:value pairs separated by space or newlines

    This returns a list of dicts {key: value, key2: value...}
    """
    with open(filename, "r") as f:
        text = f.read()

    passports = []
    parts = re.split(r"\s", text)
    current_passport = {}
    for part in parts:
        if part == "":
            # Finished passport
            passports.append(current_passport)
            current_passport = {}
            continue
        else:
            key, value = part.strip().split(":", 1)
            current_passport[key] = value

    # If we did not finish on an empty line, so we close the last one
    if current_passport != {}:
        passports.append(current_passport)
    return passports


def check_fields(passport, validators=None):
    """
    The list of fields are
        byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
        cid (Country ID)

    Returns True if the passport is valid (no missing fields except cid)
    """
    for field in REQUIRED:
        if field not in passport:
            return False
        # Validate the Field
        value = passport[field]
        if validators is not None:
            valid_fn = validators[field]
            if not valid_fn(value):
                return False
    return True


def solve(passports, validators=None):
    valid_passports = len(
        list(filter(partial(check_fields, validators=validators), passports))
    )
    return valid_passports


# Parsed input
passports = parse_input("input4.txt")

# Solution for #1
print(solve(passports))


def digit_validators(n_digits, min, max):
    def validator(x):
        if not x.isdigit():
            return False
        if not len(x) == n_digits:
            return False
        value = int(x)
        return min <= value <= max
    return validator


cm_validator = digit_validators(3, 150, 193)
in_validator = digit_validators(2, 59, 76)


def height_validator(height):
    units = height[-2:]
    value = height[:-2]
    if units == "cm":
        return cm_validator(value)
    elif units == "in":
        return in_validator(value)
    else:
        return False


def hair_color_validator(hcl):
    return bool(re.search(r"#[0-9a-f]{6}", hcl))


# Solution for #2
validators = {
    "byr": digit_validators(4, 1920, 2002),
    "iyr": digit_validators(4, 2010, 2020),
    "eyr": digit_validators(4, 2020, 2030),
    "hgt": height_validator,
    "hcl": hair_color_validator,
    "ecl": lambda x: x in HAIR_COLORS,
    "pid": digit_validators(9, 0, 999999999),
}

print(solve(passports, validators=validators))
