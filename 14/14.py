import re
import numpy as n
WIDTH = 101 # 11 for small input
HEIGHT = 103 # 7 for small input

def extract_numbers(line):
    pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
    match = re.search(pattern, line)
    return list(int(i) for i in match.group(1,2,3,4))

def parse():
    return open("input.txt").read().splitlines()

def make_move(robots):
    for r in robots:
        r[0] = (r[0] + r[2]) % WIDTH
        r[1] = (r[1] + r[3]) % HEIGHT

def print_board(robots,s):
    board =[['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for r in robots:
        board[r[1]][r[0]]= "*"
    for i in range(len(board)):
        board[i] = "".join(board[i])
        board[i]+="X" #"\n"
    for l in board:
        print(l)
    # open(f"{s}.txt","w").writelines(board)


def write_board(robots):
    pass

def get_safety_factor(robots):
    Q1 = Q2 = Q3 = Q4 = 0 # We use the classic geometric quadrant numeration
    for r in robots:
        if (r[0] > WIDTH // 2) and (r[1]< HEIGHT//2):
            Q1+=1
        if (r[0] < WIDTH // 2) and (r[1] < HEIGHT // 2):
            Q2+=1
        if (r[0] < WIDTH // 2) and (r[1] > HEIGHT // 2):
            Q3+=1
        if (r[0] > WIDTH // 2) and (r[1] > HEIGHT // 2):
            Q4+=1
    return Q1*Q2*Q3*Q4

def solve_first(lines):
    robots = list()
    for l in lines:
        robots.append(extract_numbers(l))
    seconds = 10000
    print(robots[0])
    for s in range(seconds):
        make_move(robots)
        if s % 101 == 3:
            print(s)
            print_board(robots,s)
            print()
            input()
    return get_safety_factor(robots)


print(solve_first(parse()))


2528
2629