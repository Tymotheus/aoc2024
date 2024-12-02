import logging
import math

# logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def parse():
    return open("input.txt").read().splitlines()

def most_common(lst):
    '''Since one erroneous record is allowed, we need to check 3 elements to denote potential monotonicity.'''
    return max(set(lst), key=lst.count)

def is_allowed(a, b, sign):
    if math.copysign(1, b-a) == sign and (abs(b-a)>0) and (abs(b-a)<4):
        return True
    else:
        return False

def solve_first(lines):
    levels = [l.split(' ') for l in lines]
    levels = [[int(i) for i in l] for l in levels]
    counter = 0
    for l in levels:
        signum = math.copysign(1, l[1]-l[0])
        correct = True
        for i in range(1,len(l)):
            if is_allowed(l[i-1], l[i], signum):
                pass
            else:
                correct = False
                break
        if correct:
            counter+=1
    return counter


def solve_second(lines):
    '''
    Our solution needs to be resilient and correct for the following edge cases:
    3 1 2 3
    1 -2 2 3
    1 2 3 8
    3 2 4 5 10
    :param lines:
    :return:
    '''
    levels = [l.split(' ') for l in lines]
    levels = [[int(i) for i in l] for l in levels]
    counter = 0
    for l in levels:
        signum = most_common(list(map(lambda x: math.copysign(1,x), [l[1]-l[0], l[2]-l[1], l[3]-l[2]])))
        correct = True
        number_dumped = 0
        i = 1
        while i < len(l):
            # Too much dumping
            if number_dumped > 1:
                correct = False
                break
            # Happy scenario, all is correct
            if is_allowed(l[i-1],l[i], signum):
                i+=1
                continue
            # We got to the last element of the list
            elif i+1 >= len(l):
                # If we havent dumped anything yet - then all is good
                # If we have, it is too much dumping
                if number_dumped > 0:
                    correct = False
                break
            # Case acceptable for the first element too
            elif is_allowed(l[i-1], l[i+1], signum):
                l.pop(i)
                number_dumped += 1
                i = 1 # iterate once more
            elif is_allowed(l[i], l[i+1], signum):
                l.pop(i-1)
                number_dumped += 1
                i = 1 # iterate once more
            else:
                correct = False
                break
        if correct:
            counter += 1
    return counter


print(solve_first(parse()))
print(solve_second(parse()))