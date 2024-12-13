# Rules: if a field A is adjacent to X number of fields A, it adds total perimeter of:
# X=0 - 4
# X=1 - 3
# X=2 - 2
# X=3 - 1
# X=4 -0
# So we can count the neighbours, take the rule from above
import symbol


#Rules while traversing:
#If first field of type like that assign label (label might be current position of field)
# If field has upper or left neighbour (traversing from top to bottom and left to right) take its label
# Then Add each shape (denoted by upper-leftmost square) to dictionary or sth and calculate/update the perimeter
# with rules from the first lines
# In fact all can be done with one traversal of the map. Complexity: 4*n^2 where n is the side of the whole square field

def parse():
    return open("input_small.txt").read().splitlines()

def count_neighbours(row, column, board): #This is not pure function
    """Checks for adjacency. Each adjacent tile removes one side from fence.
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

def tag_neighbours(row, column, board, pointer_board, father): #rn this is not enough, tagging immediate neighbours is not enough.
    # Look at the F fields in the medium example on the right, it is too far for the left elements to know they are in already existing grouo
    # Maybe add some reconciliation? If 2 groups turn out to be one group...?
    char = board[row][column]
    pointer_board[row][column] = father
    if row > 0:
        if board[row - 1][column] == char:
            pointer_board[row - 1][column] = father
    if row < len(board) - 1:
        if board[row + 1][column] == char:
            pointer_board[row + 1][column] = father
    if column > 0:
        if board[row][column - 1] == char:
            pointer_board[row][column - 1] = father
    if column < len(board[0]) - 1:
        if board[row][column + 1] == char:
            pointer_board[row][column + 1] = father
    return pointer_board

def is_pioneer_tile(row, column, board, pointer_board) -> bool:
    # Checks if the tile is first in the group
    char = board[row][column]
    if row > 0 and board[row - 1][column] == char and pointer_board[row - 1][column]:
        return False
    elif column > 0 and board[row][column - 1] == char and pointer_board[row][column - 1]:
        return False
    elif column < len(board[0]) - 1 and board[row][column + 1] == char and pointer_board[row][column + 1]:
        return False
    elif row < len(board) - 1 and board[row + 1][column] == char and pointer_board[row + 1][column]:
        return False
    return True

def get_group(row, column, board, pointer_board):
    # If a tile belongs to a group, returns group's key
    char = board[row][column]
    if row > 0 and board[row - 1][column] == char and pointer_board[row - 1][column]:
        return pointer_board[row - 1][column]
    if column > 0 and board[row][column - 1] == char and pointer_board[row][column - 1]:
        return pointer_board[row][column - 1]
    if column < len(board[0]) - 1 and board[row][column + 1] == char and pointer_board[row][column + 1]:
        return pointer_board[row][column + 1]
    if row < len(board) - 1 and board[row + 1][column] == char and pointer_board[row + 1][column]:
        return pointer_board[row + 1][column]
    return None

def get_tile_map(board, pointer_board) -> dict[tuple[int], list[int]]:
    shapes = {} # Keys are gonna be tuples
    for row in range(len(board)):
        for col in range(len(board[0])):
            if not pointer_board[row][col]:
                shapes[(row, col)] = [count_neighbours(row, col, board), 1]
                pointer_board[row][col] = (row, col)
                pointer_board = tag_neighbours(row, col, board, pointer_board, (row, col))
            else:
                continue #already marked
                pointer_board = tag_neighbours(row, col, board, pointer_board, get_group(row, col, board, pointer_board)) #this field now points at its "father"
                shapes[get_group(row, col, board, pointer_board)][0] += count_neighbours(row, col, board) # TODO: problem is in tagging itself
                shapes[get_group(row, col, board, pointer_board)][1] += 1
    return shapes

def get_total_cost(shapes):
    acc = 0
    for cords in shapes:
        acc += shapes[cords][0] * shapes[cords][1]
    return acc

def solve_first(lines):
    acc = 0
    # Shape is a collection of tiles
    # We store shapes in the dictionary where every key is the upper-most, and then left-most tile of the shape
    # that uniquely defines the whole shape. Each value is a list: [perimeter, surface].
    board = [[c for c in l] for l in lines]
    pointer_board = [[None for _ in l ]for l in lines] # Each fields points to the its shape-definining tile position
    shapes = get_tile_map(board, pointer_board)
    print(shapes)
    return get_total_cost(shapes)


def solve_second(lines):
    acc = 0
    return acc


print(solve_first(parse()))
# print(solve_second(parse()))