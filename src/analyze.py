import sys
import os

DEBUG = False 

parsing_table = {
    'S': {
        'a' : [ 'a', 'Z' ],
    },
    'Z': {
        'a': [ 'a', 'C', 'B' ],
        'b': [ 'b', 'A' ],
        'c': [ 'c', 'A', 'B' ],
    },
    'A': {
        'a': [ 'a', 'Aprime' ],
    },
    'Aprime': {
        'a': [ 'a', 'Aprime' ],
        'b': [ '' ],               # '' is an 'empty' sign
        '$': [ '' ],
    },
    'B': {
        'b': [ 'b', 'Bprime' ],
    },
    'Bprime': {
        'b': [ 'b', 'Bprime' ],
        '$': [ '' ],
    },
    'C': {
        'c': [ 'c', 'Cprime' ],
    },
    'Cprime': {
        'b': [ '' ],
        'c': [ 'c', 'Cprime' ],
    },
}


def analyze(s: str):
    global DEBUG
    i = 0
    expr_stack = [ 'S' ]

    while True:
        if DEBUG: print(f'Current state: string: {s[i:]}, stack: {expr_stack}')

        if s[i] == '$' and len(expr_stack) == 0:
            return True

        top = expr_stack.pop()

        if DEBUG: print(f'Current state: string: {s[i:]}, stack: {expr_stack}')

        if top == '':
            continue
        if top[0].isupper():
            if top not in parsing_table:
                return False

            if s[i] not in parsing_table[top]:
                return False

            expr_stack.extend(parsing_table[top][s[i]][::-1])
            continue

        if top[0].islower():
            if top == s[i]:
                i += 1
                continue
            else:
                return False


def main(argv):
    global DEBUG

    if len(argv) < 2:
        return 1

    if argv[1] == '-g':
        DEBUG = True
        print(f'Result: {analyze(argv[2] + '$')}')
        return 0

    DEBUG = False
    print(f'Result: {analyze(argv[1] + '$')}')

    return 0

if __name__ == '__main__':
    exit(main(sys.argv))
