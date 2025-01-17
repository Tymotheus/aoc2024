from treelib import Node, Tree
from functools import cache

def parse():
    lines = open("input.txt").read().splitlines()
    towels = [ t.strip() for t in lines[0].split(",")]
    patterns = lines[2:]
    return towels, patterns

def try_pattern(pattern, towels) -> bool:
    """Verify if a given pattern can be built using the given towels."""
    if pattern == "": # We have come to the point when the pattern has been completed! :)
        return True
    for towel in towels:
        if pattern.startswith(towel):
            if try_pattern(pattern[len(towel):], towels): return True # Happy case
            else: continue
        continue
    return False

def check_tree_pattern(pattern, towel_tree, parent) -> bool:
    if pattern == "": return True
    for child in towel_tree.children(parent):
        if pattern.startswith(child.tag):
            if check_tree_pattern(pattern[len(child.tag):], towel_tree, '.'): return True #We have a match, we continue the search for the substring
            elif check_tree_pattern(pattern, towel_tree, child.tag): return True # No match, we try to find a match within children of the node
    return False

def build_towel_tree(towels: list) -> Tree:
    tree = Tree()
    tree.create_node(".", ".")
    towels.sort(key=lambda t: (len(t), t))
    for towel in towels:
        parent = '.'
        for i in range(len(towel)):
            if tree.contains(towel[:i]):
                parent = towel[:i]
        tree.create_node(towel, towel, parent=parent)
    return tree

def solve_first_recurrent(towels, patterns): # complexityL t * p * a for t-number of towels, p - number of patterns * a - average number of tokens(towels) in a pattern
    acc = 0
    acc = 0
    print(towels)
    print(patterns)
    for pattern in patterns:
        if try_pattern(pattern, towels): acc+=1
    return acc


def solve_first_tree_recurrent(towels, patterns): #complexity: log5(t) * p * a for t-number of towels, p - number of patterns * a - average number of tokens(towels) in a pattern
    acc = 0
    tree = build_towel_tree(towels)
    for pattern in patterns:
        if check_tree_pattern(pattern, tree, '.'):
            acc += 1
    return acc

def solve_first(towels, patterns):
    acc = 0
    return acc

def solve_second(patterns, towels):
    """Solution by Piotr Piątkowski. Here the naming convention is reverted. Towels (bigger)consist of patterns (smaller)"""
    acc=0

    @cache
    def valid(towel):
        if towel == "":
            return 1
        c = 0
        for p in patterns:
            if towel.startswith(p):
                c+= valid(towel[len(p):])
        return c
    vals = []
    for t in towels:
        vals.append(valid(t))
    print(sum(v>0 for v in vals))
    print(sum(vals))
    return acc


print(solve_first(*parse()))
print(solve_second(*parse()))