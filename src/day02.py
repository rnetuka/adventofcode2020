# --- Day 2: Password Philosophy ---

import re
from collections import namedtuple

Policy = namedtuple('PasswordPolicy', ('n', 'm', 'letter', 'password'))


def parse(input, mod=lambda x: x):
    if search_result := re.compile('(\\d+)-(\\d+) (\\w): (\\w+)').search(input):
        n = mod(int(search_result.group(1)))
        m = mod(int(search_result.group(2)))
        letter = search_result.group(3)
        password = search_result.group(4)
        return Policy(n, m, letter, password)


def is_password_valid(input):
    min, max, letter, password = parse(input)
    count = password.count(letter)
    return min <= count <= max


def is_password_valid_reworked(input):
    i, j, letter, password = parse(input, mod=lambda x: x - 1)
    cond_i = password[i] == letter
    cond_j = password[j] == letter
    return cond_i ^ cond_j


def count_if(list, test):
    return sum(test(item) for item in list)


if __name__ == '__main__':
    with open('../res/day02.txt') as file:
        passwords = file.read().splitlines()

    print('Day 2: Password Philosophy')
    print('--------------------------')

    print(f'Valid passwords: {count_if(passwords, is_password_valid)}')
    print(f'Valid passwords: {count_if(passwords, is_password_valid_reworked)}')