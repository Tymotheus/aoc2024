import re
import numpy as np


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

def solve_one_machine(lines, is_part_two=False):
    # Returns solution for linear equation given by specification of buttons
    a_x, a_y = extract_numbers(lines[0])
    b_x, b_y = extract_numbers(lines[1])
    p_x, p_y = extract_numbers(lines[2])
    coefficients = np.array([[a_x, b_x], [a_y, b_y]], dtype=np.int64) # Units of move for one push of button
    constants = np.array([p_x, p_y], dtype=np.int64) # Desired position for claw location
    if is_part_two:
        constants+= 10**13
    return np.linalg.solve(coefficients, constants)

def solve_first():
    lines = open("input.txt").read().splitlines()
    tokens_one = 0
    tokens_two = 0
    for i in range(0, len(lines), 4): #We grab group of lines for every machine, including trailing newline
        solution_one = solve_one_machine(lines[i:i+3])
        if np.allclose(solution_one, np.round(solution_one)): # There is a solution for whole number of pushes
            tokens_one += 3*solution_one[0] + solution_one[1] # Adding cost in tokens of pushing each button
        solution_two = solve_one_machine(lines[i:i+3], True)
        # for i in solution_two:
        #     print("{:.8f}".format(i))
        if np.allclose(solution_two, np.round(solution_two),rtol=1e-14,atol=1e-08):
            tokens_two += 3*solution_two[0] + solution_two[1]
    print(f"Tokens for part one: {tokens_one}")
    print(f"Tokens for part two: {tokens_two}")


solve_first()