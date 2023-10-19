# Author: Luiz Breno Santos Costa
# Version: 0.0.0
# ALL RIGHTS RESERVED

import random

# Creating the alphabet
alphabet = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z',
    27: '0',
    28: '1',
    29: '2',
    30: '3',
    31: '4',
    32: '5',
    33: '6',
    34: '7',
    35: '8',
    36: '9'
}

letters = ''
codes = []


# Registering the data in files
def register():
    with open('files/codes.txt', 'a') as file:
        file.write(f'\n{str(codes)}:{letters}')
        file.close()

    with open('files/values.txt', 'a') as file:
        file.write(f'\n{letters}')
        file.close()


# Generating initial population
def population(chars: int):
    global letters
    i = 0
    while i < chars:
        code = random.randint(1, 36)
        codes.append(code)
        letters = letters + alphabet[code]
        i += 1

    print(f'Generating new value: {letters}')
    print(f'Generated Gene: {codes}')

    register()


def population_for_test(chars: int):
    global letters
    i = 0
    while i < chars:
        code = random.randint(1, 36)
        codes.append(code)
        letters = letters + alphabet[code]
        i += 1

    print(f'Generating new value: {letters}')
    print(f'Generated Gene: {codes}')
