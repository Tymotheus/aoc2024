"""Tried to use pandas to learn a bit and leverage some slicing - turns out without it it might have even been faster."""

import pandas as pd
import numpy as np


def solve_first():
    #Skipping parsing function to improve performance
    acc=0
    lines = open("input.txt").read().splitlines()
    rules = []
    i = iter(lines)
    sentinel = object()
    line = next(i)
    while line != '':
        rules.append((line.split("|")))
        line = next(i)
    while (l:=next(i, sentinel)) != sentinel: # testing this wild syntax
        book = l.split(",")
        correct = True
        for rule in rules:
            big_found = False
            for page in book:
                if page == rule[1]:
                    big_found = True
                if page == rule[0]: # We assume each page can appear only once in each book
                    if big_found:
                        correct = False
        #Now all the rules are checked for this booked
        if correct:
            acc += int(book[len(book)//2])
    return acc

def solve_second():
    acc = 0
    lines = open("input.txt").read().splitlines()
    rules = []
    i = iter(lines)
    sentinel = object()
    line = next(i)
    while line != '':
        rules.append((line.split("|")))
        line = next(i)
    while (l := next(i, sentinel)) != sentinel:  # testing this wild syntax
        book = l.split(",")
        correct = True
        position = None
        rule_number = 0
        while rule_number < len(rules):
            rule = rules[rule_number]
            big_found = False
            for j, page in enumerate(book):
                if page == rule[1]:
                    big_found = True
                    position = j
                if page == rule[0]:  # We assume each page can appear only once in each book
                    if big_found:
                        correct = big_found = False
                        book[position], book[j] = rule[0], rule[1] #Swap
                        position = None
                        rule_number = 0 # Recheck the rules
            rule_number += 1
        # Now all the rules are checked for this book
        if not correct:
            acc += int(book[len(book) // 2])
    return acc


print(solve_first())
print(solve_second())
