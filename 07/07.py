from collections import deque
from treelib import Node, Tree


def parse():
    return open("input.txt").read().splitlines()


def evaluate(goal, results, element, numbers):
    """Negative early stopping possible, positive early stopping impossible."""
    # print(f"results: {results}")
    # print(f"element: {element}")
    # print(f"numbers: {numbers}")

    r0 = int(str(element) + str(numbers[0]))
    if r0 > goal:
        results.append(False)
    elif len(numbers) == 1:
        results.append(True if r0 == goal else False)
    else:
        evaluate(goal, results, r0, numbers[1:])
    r1 = element * numbers[0]
    if r1 > goal:
        results.append(False)
    elif len(numbers) == 1:
        results.append(True if r1 == goal else False)
    else:
        evaluate(goal, results, r1, numbers[1:])
    r2 = element + numbers[0]
    if r2 > goal:
        return results.append(False)
    elif len(numbers) == 1:
        results.append(True if r2 == goal else False)
    else:
        evaluate(goal, results, r2, numbers[1:])
    return results


def solve_first(lines):
    acc = 0
    for l in lines:
        output, numbers = l.split(":")
        output, numbers = int(output), list(map(int, numbers.split(" ")[1:]))
        results = evaluate(output, [], numbers[0], numbers[1:])
        if True in results:
            acc += output
    return acc


def solve_second(lines):
    acc = 0
    return acc


print(solve_first(parse()))
print(solve_second(parse()))
