# Part 2
# Super ugly code but at least it doesnt work for edge cases
# Probably sth with super narrow paths or ones that are adjacent to board limits

# TODO:
# Check if can implement some walrus
# Complexity: Time: goes through all fields, each field should be visited around 2: once for tagging and once after verifying if it was already tagged so 2*n^2 for square side n
# I guess time can not go below that
# Memory: Must build 2 tables, one for board and one for pointers. Build dict of shapes, but (I think) it should sub-linearly increase with n

# Change the structure of the shapes dictionary. Should annotate somehow which field is surface and which perimeter. Enum...?
# Rules while traversing:
# If first field of type like that assign label (label might be current position of field)
# If field has upper or left neighbour (traversing from top to bottom and left to right) take its label
# Then Add each shape (denoted by upper-leftmost square) to dictionary or sth and calculate/update the perimeter
# with rules from the first lines
# In fact all can be done with one traversal of the map. Complexity: 4*n^2 where n is the side of the whole square field


class Constants:
    directions = {
        # Key: type of the cursor
        # Values: (row increment, column increment, cursor after right turn, symbol left on the passed field
        # u - moved here going upwards
        # r - rightwards
        # d - downwards
        # l - leftwards
        "^": (-1, 0, ">", "u"),
        ">": (0, 1, "v", "r"),
        "v": (1, 0, "<", "d"),
        "<": (0, -1, "^", "l"),
    }


def parse():
    return open("input.txt").read().splitlines()


def count_neighbours(row, column, board):  # This is not pure function
    """Checks for adjacency. Each adjacent tile removes one side from tile's fence.
    0 neighbours = 4 fences. 4 neighbours = no fences."""
    fences = 4
    char = board[row][column]
    if row > 0:
        if board[row - 1][column] == char:
            fences -= 1
    if row < len(board) - 1:
        if board[row + 1][column] == char:
            fences -= 1
    if column > 0:
        if board[row][column - 1] == char:
            fences -= 1
    if column < len(board[0]) - 1:
        if board[row][column + 1] == char:
            fences -= 1
    return fences


def merge_neighbours(
    row, column, board, pointer_board, shapes, father
) -> (list[tuple[int, int]], dict[tuple[int, int], list[int]]):
    # Recursive function used for identifying one whole complete shape.
    # Looks at the adjacent tiles in order to calculate the total area and perimeter
    char = board[row][column]
    pointer_board[row][column] = father
    shapes[father][0] += count_neighbours(row, column, board)  # perimeter
    shapes[father][1] += 1  # surface
    if row > 0:
        if board[row - 1][column] == char and not pointer_board[row - 1][column]:
            merge_neighbours(row - 1, column, board, pointer_board, shapes, father)
    if row < len(board) - 1:
        if board[row + 1][column] == char and not pointer_board[row + 1][column]:
            merge_neighbours(row + 1, column, board, pointer_board, shapes, father)
    if column > 0:
        if board[row][column - 1] == char and not pointer_board[row][column - 1]:
            merge_neighbours(row, column - 1, board, pointer_board, shapes, father)
    if column < len(board[0]) - 1:
        if board[row][column + 1] == char and not pointer_board[row][column + 1]:
            merge_neighbours(row, column + 1, board, pointer_board, shapes, father)
    return pointer_board, shapes


def traverse_shape(board, row, col):
    """Store your current direction. Try to go right, If possible, increase counter by 1 and turn.
    Otherwise try to go straight. If impossible, increase counter by 1 and turn left.
    Counter is the number of individual sides."""

    def is_out_of_bound(row, col):
        if (row < 0) | (col < 0) | (row > MAX_ROW) | (col > MAX_COL):
            return True
        else:
            return False

    def turn_right(direction):
        return Constants.directions[direction][2]

    def turn_left(direction):
        direction = turn_right(direction)  # XD
        direction = turn_right(direction)
        direction = turn_right(direction)
        return direction

    def is_right_free(board, row, col, direction):
        new_row, new_col = (
            row + Constants.directions[Constants.directions[direction][2]][0],
            col + Constants.directions[Constants.directions[direction][2]][1],
        )
        if is_out_of_bound(new_row, new_col):
            return False
        return board[new_row][new_col] == CHAR

    def is_straight_free(board, row, col, direction):
        new_row, new_col = (
            row + Constants.directions[direction][0],
            col + Constants.directions[direction][1],
        )
        if is_out_of_bound(new_row, new_col):
            return False
        return board[new_row][new_col] == CHAR

    def move_forward(row, col, direction):
        new_row, new_col = (
            row + Constants.directions[direction][0],
            col + Constants.directions[direction][1],
        )
        return new_row, new_col

    acc = 0
    CHAR = board[row][col]
    MAX_ROW = len(board) - 1
    MAX_COL = len(board[0]) - 1
    # We know that we start from top most and then left most element of the shape
    # So direction that we face now is DOWN
    direction = "v"
    START_ROW, START_COL = row, col
    stopping = False
    # Now the logic starts!
    while not stopping:
        if is_right_free(board, row, col, direction):
            acc += 1
            direction = turn_right(direction)
        if is_straight_free(board, row, col, direction):
            row, col = move_forward(row, col, direction)
        else:
            acc += 1
            direction = turn_left(direction)
        if row == START_ROW and START_COL == col and direction == "v":
            # We are back to the starting point
            stopping = True
    return acc


def get_tile_map(board, pointer_board) -> dict[tuple[int], list[int]]:
    shapes = {}  # Keys are gonna be tuples
    for row in range(len(board)):
        for col in range(len(board[0])):
            if not pointer_board[row][col]:
                shapes[(row, col)] = [0, 0]  # add new shape to the dictionary
                pointer_board, shapes = merge_neighbours(
                    row, col, board, pointer_board, shapes, (row, col)
                )
            else:
                continue  # Part of already marked shape
    return shapes


def get_and_solve_tile_map_2(board, pointer_board) -> dict[tuple[int], list[int]]:
    shapes = {}  # Keys are gonna be tuples
    acc = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if not pointer_board[row][col]:
                shapes[(row, col)] = [0, 0]  # add new shape to the dictionary
                sides = traverse_shape(board, row, col)
                pointer_board, shapes = merge_neighbours(
                    row, col, board, pointer_board, shapes, (row, col)
                )
                cost = sides * shapes[(row, col)][1]
                print("Sides:", sides)
                print("Cost:", cost)
                acc += cost
            else:
                continue  # Part of already marked shape
    return acc


def get_total_cost(shapes):
    acc = 0  # TODO: Candidate for walrus here?
    for cords in shapes:
        acc += shapes[cords][0] * shapes[cords][1]
    return acc


def solve_first(lines):
    # Shape is a collection of tiles
    # We store shapes in the dictionary where every key is the upper-most, and then left-most tile of the shape
    # that uniquely defines the whole shape. Each value is a list: [perimeter, surface].
    board = [[c for c in l] for l in lines]
    pointer_board = [
        [None for _ in l] for l in lines
    ]  # Each field points at its shape-defining tile position
    shapes = get_tile_map(board, pointer_board)
    # print(shapes)
    return get_total_cost(shapes)


def solve_second(lines):
    board = [[c for c in l] for l in lines]
    pointer_board = [[None for _ in l] for l in lines]
    return get_and_solve_tile_map_2(board, pointer_board)


# print(solve_first(parse()))
print(solve_second(parse()))
