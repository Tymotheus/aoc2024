import os
import re


def extract_numbers(line):
    pattern = r'X[\+=](\d+), Y[\+=](\d+)'
    match = re.search(pattern, line)

    if match:
        # Extract the numbers from the match groups
        x_number = int(match.group(1))
        y_number = int(match.group(2))
        return x_number, y_number
    else:
        return None

def parse():
    lines = open("input_small.txt").read().splitlines()
    tab = []
    for indx in range(0, len(lines), 4):
        tab.append(parse_one_machine(lines[indx:indx+4]))
    return(tab)

def parse_one_machine(lines):
    x = []
    for l in lines[:3]:
        x+=extract_numbers(l)
    return x


def solve_first(machines):
    # Shape is a collection of tiles
    # We store shapes in the dictionary where every key is the upper-most, and then left-most tile of the shape
    # that uniquely defines the whole shape. Each value is a list: [perimeter, surface].
    for i in machines: print(i)


def solve_second(lines):
    print(lines)




print(solve_first(parse()))
# print(solve_second(parse()))
