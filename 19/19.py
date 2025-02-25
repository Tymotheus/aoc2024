from treelib import Node, Tree
from functools import cache


def parse():
    lines = open("input.txt").read().splitlines()
    patterns = [t.strip() for t in lines[0].split(",")]
    towels = lines[2:]
    return patterns, towels


def solve_both(patterns, towels):
    """Solution by Piotr Piątkowski. Towels (bigger) consist of patterns (smaller)"""
    acc = 0

    @cache
    def valid(towel):
        if towel == "":
            return 1
        c = 0
        for p in patterns:
            if towel.startswith(p):
                c += valid(towel[len(p) :])
        return c

    vals = []
    for t in towels:
        vals.append(valid(t))
    print(sum(v > 0 for v in vals))
    print(sum(vals))
    return acc


print(solve_both(*parse()))
