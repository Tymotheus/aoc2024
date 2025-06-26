from functools import reduce

class Constants:
    directions = {
        #Key: type of the instruction
        #Values: (row increment, column increment)
        "^": (-1,0),
        ">": (0,1),
        "v": (1,0),
        "<": (0,-1),
    }
    OBSTACLE = '#'
    ROBOT = '@'
    BOX = 'O'

def parse():
    return open("input_small.txt").read().splitlines()

def print_board(board, pretty=False):
    if pretty:
        for i, line in enumerate(board):
            print(reduce(lambda x, y: x + y, line))
    else:
        for line in board:
            print(line)

def find_cursor(board):
    pos_r = pos_c = None
    for r, line in enumerate(board):
        for c, field in enumerate(line):
            if field == Constants.ROBOT:
                pos_r, pos_c = r, c
    return pos_r, pos_c



def check_for_moving_box():
    """
    Check if the box can be moved, if it can be moved, move it.
    If it cannot be moved, do not do anything.
    """
    # This is a placeholder for the logic that checks if the box can be moved
    # and moves it if possible. The actual implementation will depend on the
    # specific rules of the game or simulation.
    pass

def move_forward(board, pos_r, pos_c, nex_r, nex_c):
    # move all the boxes if applicable:
    # ......
    # if not, just overwrite the current position with the next position
    board[nex_r][nex_c] = "@"
    board[pos_r][pos_c] = '.'
    return board

def get_next_position(instruction, pos_r: int, pos_c: int) -> tuple[int, int]:
    nex_r, nex_c = pos_r + Constants.directions[instruction][0], pos_c + Constants.directions[instruction][1]
    return nex_r, nex_c


def make_move(board, instruction, pos_r: int = None, pos_c: int = None) -> tuple[list, int, int]:
    """
    1. Get or detect where is the current position
    3. Check if there is obstacle or move forward
    :param board:
    :param instruction: the instruction to be executed
    :param pos_r:
    :param pos_c:
    :return: return final position of the cursor
    """
    # The position was not passed with the arguments, we need to find it
    if None in (pos_r, pos_c):
        pos_r, pos_c = find_cursor(board)
    nex_r, nex_c = get_next_position(instruction, pos_r, pos_c)
    if board[nex_r][nex_c] == Constants.OBSTACLE:
        pass # Do not move, wait for the next instruction
    if board[nex_r][nex_c] == Constants.BOX:
        # If there is a box we need to check if we can move it
        check_for_moving_box()
    else:
        board = move_forward(board, pos_r, pos_c, nex_r, nex_c)
        return board, nex_r, nex_c


def solve_first(lines):
    board = list()
    instructions = list()
    for l in lines:
        if l == "": break
        else:
            board.append([field for field in l])
    for l in lines[len(board)+1:]:
        instructions.append(l)
    instructions = reduce(lambda x, y: x + y, instructions) #make instructions a single string
    print(board)
    print(instructions)
    acc = 0
    end = False
    iteration = 1
    print_board(board)
    print(find_cursor(board))
    for i in instructions:
        make_move(board, i)
        pass
    # while not end:
    #     # The input guarantees that the loop will eventually stop
    #     iteration+=1
    #     # print("\n\n")
    #     # print(iteration)
    #     for i, line in enumerate(board):
    #         # print(line)
    #
    #         for j, field in enumerate(line):
    #             if field in Constants.directions.keys():
    #                 next_position = (i + Constants.directions[field][0], j + Constants.directions[field][1])
    #                 if 0 <= next_position[0] < len(board) and 0 <= next_position[1] < len(board[0]):
    #                     # not leaving the map
    #                     if board[next_position[0]][next_position[1]] == '#':
    #                         board[i][j] = Constants.directions[field][2]
    #                         continue
    #                     else:
    #                         board[i][j] = 'X'
    #                         board[next_position[0]][next_position[1]] = field
    #                 else: # leaving the board
    #                     end = True
    # # Print the final map
    # for i, line in enumerate(board):
    #     print(line)
    #     for j, field in enumerate(line):
    #         if field == 'X': acc+=1
    return acc+1 #one accounting for field just before exiting the map


def solve_second(lines, interactive = False):
    acc = 0
    return acc


print(solve_first(parse()))
# print(solve_second(parse(), interactive = True))