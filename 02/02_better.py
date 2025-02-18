"""
This solution is inspired by Jonathan Paulson.
"""

import logging

logging.basicConfig(level=logging.INFO)


def parse():
    return open("input.txt").read().splitlines()


def is_good(xs):
    inc_or_dec = xs == sorted(xs) or xs == sorted(xs, reverse=True)
    correct = True
    for i in range(len(xs) - 1):
        diff = abs(xs[i] - xs[i + 1])
        if not 1 <= diff <= 3:
            correct = False
    return inc_or_dec and correct


def solve_second(lines):
    levels = [l.split(" ") for l in lines]
    levels = [[int(i) for i in l] for l in levels]
    counter = 0
    for l in levels:
        correct = False
        for i in range(len(l)):
            xs = l[:i] + l[i + 1 :]
            if is_good(xs):
                correct = True
        if correct:
            counter += 1
    return counter


print(solve_second(parse()))
