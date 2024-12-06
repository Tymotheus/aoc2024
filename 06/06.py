from collections import deque
from treelib import Node, Tree

directions = {
    "^": (-1,0, ">"),
    ">": (0,1, "v"),
    "v": (1,0, "<"),
    "<": (0,-1, "^"),
}

def parse():
    return open("input.txt").read().splitlines()


def solve_first(lines):
    board = [[field for field in l] for l in lines]
    acc = 0
    end = False
    iteration = 0
    while not end:
        # The input guarantees that the loop will eventually stop
        iteration+=1
        # print("\n\n")
        # print(iteration)
        for i, line in enumerate(board):
            # print(line)

            for j, field in enumerate(line):
                if field in directions.keys():
                    next_position = (i + directions[field][0], j + directions[field][1])
                    if 0 <= next_position[0] < len(board) and 0 <= next_position[1] < len(board[0]):
                        # not leaving the map
                        if board[next_position[0]][next_position[1]] == '#':
                            board[i][j] = directions[field][2]
                            continue
                        else:
                            board[i][j] = 'X'
                            board[next_position[0]][next_position[1]] = field
                    else: # leaving the board
                        end = True
    # Print the final map
    for i, line in enumerate(board):
        print(line)
        for j, field in enumerate(line):
            if field == 'X': acc+=1
    return acc+1 #one accounting for field just before exiting the map


def solve_second(lines):
    acc = 0
    return acc


print(solve_first(parse()))
print(solve_second(parse()))