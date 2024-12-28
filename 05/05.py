from collections import deque
# from treelib import Node, Tree


def parse():
    return open("input.txt").read().splitlines()


def solve_first(lines):
    acc = 0
    rules = [[set()]]
    print(rules)
    for l in lines:
        if l == '':
            break
        left, right = l.split('|')
        left, right = int(left), int(right)
        print(left,right)
        lcords, rcords = None, None
        for num, r in enumerate(rules): #we search through all the list of rules
            for senum, se in enumerate(r): #we look at each set in the list of rules
                if left in se:
                    lcords = num, senum
                if right in se:
                    rcords = num, senum

        if lcords is None and rcords is None:
            rules.append([{left}, {right}])
        elif lcords is None:
            if rcords[1] == 0:
                rules[rcords[0]] = [set().add(left), *rules[rcords[0]]] #we insert new set at the beginning
            else:
                rules[rcords[0]][rcords[1]-1].add(left) # we add left element immediately to the left of the right element
        elif rcords is None:
            if lcords[1] == len(rules[lcords[0]]): # we insert new set at the end
                rules[lcords[0]] = [*rules[lcords[0]], set.add(right) ]
            else:
                rules[lcords[0]][lcords[1]+1].add(right) # we add right element immediately to the right of the left
        else: # Both elements are present, need to merge 2 lists, for sure they should be 2 different lists (?)
            pass
    print(rules)


    ordering = [{1,2}, {3,4}]
    print(ordering)
    return acc


def solve_second(lines):
    acc = 0
    return acc


print(solve_first(parse()))
# print(solve_second(parse()))