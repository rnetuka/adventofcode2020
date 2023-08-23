# --- Day 4: Passport Processing ---

import re
from src.util import count_if


class Passport:

    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None

    @staticmethod
    def parse(string):
        p = Passport()
        for part in string.split():
            key, value = part.split(':')
            if key in ('byr', 'iyr', 'eyr'):
                value = int(value)
            p.__setattr__(key, value)
        return p

    def is_valid(self, strict=False):
        for attr, value in self.__dict__.items():
            if attr == 'cid':
                continue
            if not value:
                return False
            if strict and not validate(attr, value):
                return False
        return True


class PassportBuilder:

    def __init__(self):
        self.clear()

    def append(self, data):
        if self.str:
            self.str += ' '
        self.str += data

    def clear(self):
        self.str = ''

    def build(self):
        p = Passport.parse(self.str)
        self.clear()
        return p

    def __bool__(self):
        return bool(self.str)


def validate(attr, value):
    return {
        'byr': lambda x: 1920 <= x <= 2002,
        'iyr': lambda x: 2010 <= x <= 2020,
        'eyr': lambda x: 2020 <= x <= 2030,
        'hgt': lambda x: (size := int(x[:-2])) and
                         x.endswith('cm') and 150 <= size <= 193 or
                         x.endswith('in') and 59 <= size <= 76,
        'hcl': lambda x: re.match('^#[a-f0-9]{6}$', x),
        'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda x: re.match('^[0-9]{9}$', x),
        'cid': lambda x: True
    }[attr](value)


def load_passports(path):
    passports = []
    with open(path) as file:
        b = PassportBuilder()
        while line := file.readline():
            if line == '\n':
                passports.append(b.build())
            else:
                b.append(line.rstrip())
    if b:
        passports.append(b.build())
    return passports


if __name__ == '__main__':
    print('Day 4: Passport Processing')
    print('--------------------------')

    passports = load_passports('../res/day04.txt')

    print(f'Valid passports: {count_if(passports, Passport.is_valid)}')
    print(f'Valid passports (strict): {count_if(passports, lambda x: x.is_valid(strict=True))}')
