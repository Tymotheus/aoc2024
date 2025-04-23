from functools import cache
from math import log10
import cProfile


def parse():
    return open("input.txt").read().split()


@cache
def get_num_digits(n: int):
    if n > 0:
        return int(log10(n)) + 1
    elif n == 0:
        return 1
    else:
        return None


@cache
def compute_length_for_element(n: int, epochs: int):
    """Takes a value and number of epochs. Returns number of elements for a list after number of epochs."""
    if epochs == 0:
        return 1
    if n == 0:
        return compute_length_for_element(1, epochs - 1)
    elif get_num_digits(n) % 2 == 0:
        left_el = n // (10 ** int(get_num_digits(n) / 2))
        right_el = n % (10 ** int(get_num_digits(n) / 2))
        return compute_length_for_element(
            left_el, epochs - 1
        ) + compute_length_for_element(right_el, epochs - 1)
    else:
        return compute_length_for_element(n * 2024, epochs - 1)


def solve(stones, epochs: int):
    acc = 0
    for stone in stones:
        acc += compute_length_for_element(int(stone), epochs)
    return acc


print(solve(parse(), epochs=25))
print(solve(parse(), epochs=75))
# print(cProfile.run('solve(parse(),75)'))
