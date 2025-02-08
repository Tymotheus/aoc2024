from functools import reduce

class Constants:
    directions = {
        #Key: type of the cursor
        #Values: (row increment, column increment, cursor after right turn, symbol left on the passed field
        # u - moved here going upwards
        # r - rightwards
        # d - downwards
        # l - leftwards
        "^": (-1,0, ">", "u"),
        ">": (0,1, "v", "r"),
        "v": (1,0, "<", "d"),
        "<": (0,-1, "^", "l"),
    }
    OBSTACLE = '#'

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
            if field in Constants.directions.keys():
                pos_r, pos_c = r, c
    return pos_r, pos_c

def check_for_cycle(board, pos_r, pos_c):
    """
    1. Look right, (so column to up if you move left, row to right if you go up etc.)
    2. Check field by field until you find an obstacle or desired field.
    3. If there is a desired field, great! We have found a cycle! Increment the accumulator
    4. If there is no desired field until the obstacle - there will be no cycle.
    :param board:
    :param pos_r:
    :param pos_c:
    :return:
    """
    pass

def turn_right(board, pos_r, pos_c):
    """Overwrite the board changing direction"""
    cursor = board[pos_r][pos_c]
    board[pos_r][pos_c] = Constants.directions[cursor][2]
    return board

def check_for_border(board, pos_r, pos_c):
    """Check if your next move is not gonna make you go overboard"""
    if True:
        end = True
    else:
        end = False
    pass

def move_forward(board, pos_r, pos_c, nex_r, nex_c):
    # Remember to overwrite new field and clean the one that you have just been to
    cursor = board[pos_r][pos_c]
    board[nex_r][nex_c] = cursor
    board[pos_r][pos_c] = Constants.directions[cursor][3]
    return board

def get_next_position(board, pos_r: int, pos_c: int) -> tuple[int, int]:
    print(pos_r, pos_c)
    cursor = board[pos_r][pos_c]
    print(cursor)
    nex_r, nex_c = pos_r + Constants.directions[cursor][0], pos_c + Constants.directions[cursor][1]
    return nex_r, nex_c


def make_move(board, pos_r: int = None, pos_c: int = None) -> tuple[list, int, int]:
    """
    1. Get or detect where is the current position
    2. Check for cycle, if so, increment accumulator
    3. Check if there is obstacle or move forward
    :param board:
    :param pos_r:
    :param pos_c:
    :return: return final position of the cursor
    """
    # The position was not passed with the arguments, we need to find it
    if None in (pos_r, pos_c):
        pos_r, pos_c = find_cursor(board)
    check_for_cycle(board, pos_r, pos_c)
    nex_r, nex_c = get_next_position(board, pos_r, pos_c)
    if board[nex_r][nex_c] == Constants.OBSTACLE:
        board = turn_right(board, pos_r, pos_c)
        return board, pos_r, pos_c
    else:
        check_for_border(board, pos_r, pos_c)
        board = move_forward(board, pos_r, pos_c, nex_r, nex_c)
        return board, nex_r, nex_c




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
                if field in Constants.directions.keys():
                    next_position = (i + Constants.directions[field][0], j + Constants.directions[field][1])
                    if 0 <= next_position[0] < len(board) and 0 <= next_position[1] < len(board[0]):
                        # not leaving the map
                        if board[next_position[0]][next_position[1]] == '#':
                            board[i][j] = Constants.directions[field][2]
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


def solve_second(lines, interactive = False):
    #global board # Should it be global?
    board = [[field for field in l] for l in lines]
    acc = 0
    end = False
    iteration = 0
    pos_r = pos_c = None
    while not end:
        iteration += 1
        if interactive:
            print_board(board)
            input("Press Enter to continue...") # Make the simulation interactive
        board, pos_r, pos_c = make_move(board, pos_r, pos_c)
        if iteration > 100:
            end = True
    # Print the final map
    print_board(board, pretty=True)
    return acc


# print(solve_first(parse()))
print(solve_second(parse(), interactive = True))