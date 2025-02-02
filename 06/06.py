from functools import reduce

directions = {
    "^": (-1,0, ">"),
    ">": (0,1, "v"),
    "v": (1,0, "<"),
    "<": (0,-1, "^"),
}

def parse():
    return open("input_small.txt").read().splitlines()


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
    board = [[field for field in l] for l in lines]
    acc = 0
    end = False
    iteration = 0
    met_crossing = False
    while not end:
        # The input guarantees that the loop will eventually stop
        iteration += 1
        print(iteration)
        for l in board: print(l)
        input("Press Enter to continue...")
        for i, line in enumerate(board):
            for j, field in enumerate(line):
                if field in directions.keys():
                    next_position = (i + directions[field][0], j + directions[field][1])
                    if 0 <= next_position[0] < len(board) and 0 <= next_position[1] < len(board[0]):
                        # not leaving the map
                        if board[next_position[0]][next_position[1]] == '#':
                            board[i][j] = directions[field][2]
                            continue
                        else:
                            if met_crossing:
                                board[i][j] = '+'
                                met_crossing = False
                            else:
                                board[i][j] = '-' if directions[field][0] == 0 else '|'
                            if board[next_position[0]][next_position[1]] in ('-', '|'):
                                met_crossing = True
                            # The field hasn't been visited yet. We mark it as horizontally passed - or vertically passed |
                            board[next_position[0]][next_position[1]] = field
                    else:  # leaving the board
                        end = True
    # Print the final map
    for i, line in enumerate(board):
        print(reduce(lambda x,y: x+y, line))
        for j, field in enumerate(line):
            if field == 'X': acc += 1
    return acc + 1  # one accounting for field just before exiting the map


# print(solve_first(parse()))
print(solve_second(parse()))