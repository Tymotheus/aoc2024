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
    SPACE = '.'

def parse():
    lines = open("input.txt").read().splitlines()
    board = list()
    instructions = list()
    for l in lines:
        if l == "":
            break
        else:
            board.append([field for field in l])
    for l in lines[len(board) + 1:]:
        instructions.append(l)
    instructions = reduce(lambda x, y: x + y, instructions)  # make instructions a single string
    return board, instructions

def print_board(board, pretty=False):
    if pretty:
        for i, line in enumerate(board):
            print(reduce(lambda x, y: x + y, line))
    else:
        for line in board:
            print(line)
    print()

def find_cursor(board):
    pos_r = pos_c = None
    for r, line in enumerate(board):
        for c, field in enumerate(line):
            if field == Constants.ROBOT:
                pos_r, pos_c = r, c
    return pos_r, pos_c


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

def attempt_push(board, instruction, pos_r, pos_c, nex_r, nex_c):
    # If there is a box we need to check if we can move it
    front_box_r, front_box_c = nex_r, nex_c
    stopping = False
    while not stopping:
        nex_r, nex_c = get_next_position(instruction, nex_r, nex_c)
        if board[nex_r][nex_c] == Constants.OBSTACLE:
            stopping = True
        elif board[nex_r][nex_c] == Constants.SPACE:
            board[nex_r][nex_c] = Constants.BOX
            move_forward(board, pos_r, pos_c, front_box_r, front_box_c)
            pos_r, pos_c = front_box_r, front_box_c
            stopping = True
        elif board[nex_r][nex_c] == Constants.BOX:
            continue
        else:
            raise Exception("Field on the board undefined")
    return board, pos_r, pos_c

def make_move(board: list[list], instruction: str, pos_r: int = None, pos_c: int = None) -> tuple[list[list], int, int]:
    """
    1. Get or detect where is the current position
    2. Check what is the next field for robot based on instruction
    3. Perform a proper move accordingly
    :param board:
    :param instruction: the instruction to be executed
    :param pos_r:
    :param pos_c:
    :return: return the board and position r and c after moving
    """
    if None in (pos_r, pos_c):
        pos_r, pos_c = find_cursor(board)
    nex_r, nex_c = get_next_position(instruction, pos_r, pos_c)
    if board[nex_r][nex_c] == Constants.SPACE:
        board = move_forward(board, pos_r, pos_c, nex_r, nex_c)
        pos_r, pos_c = nex_r, nex_c
    elif board[nex_r][nex_c] == Constants.OBSTACLE:
        pass # Do not move, wait for the next instruction
    elif board[nex_r][nex_c] == Constants.BOX:
        # If there is a box we need to check if we can move it
        board, pos_r, pos_c = attempt_push(board, instruction, pos_r, pos_c, nex_r, nex_c)
    else:
        raise Exception("Field on the board undefined")
    return board, pos_r, pos_c

def get_gps_sum(board):
    gps_sum = 0
    for r, l in enumerate(board):
        for c, field in enumerate(l):
            if field == Constants.BOX:
               gps_sum += 100 * r + c
    return gps_sum

def solve_first():
    board, instructions = parse()
    iteration = 1
    pos_r = pos_c = None
    # print_board(board)
    for i in instructions:
        # print(iteration)
        board, pos_r, pos_c = make_move(board, i, pos_r, pos_c)
        # print_board(board)
        iteration += 1
    return get_gps_sum(board)



def solve_second(lines, interactive = False):
    acc = 0
    return acc



print(solve_first())
# print(solve_second(parse(), interactive = True))