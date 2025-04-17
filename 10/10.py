
def parse():
    return open("input_small.txt").read().splitlines()

def is_in_bound(cord_x, cord_y, board):
    if cord_x>=len(board) or cord_x <0 or cord_y >=len(board[0]) or cord_y < 0:
        return False
    else:
        return True

def follow_trail(cord_x, cord_y, board, previous_height, acc):
    current_height = int(board[cord_x][cord_y])
    if current_height != previous_height + 1: # Not a part of a good trail
        return acc
    elif board[cord_x][cord_y] == '9':
        print(f"Found the end of a trail! x {cord_x} y {cord_y}")
        return acc+1
    for i in (-1, 1):
        if is_in_bound(cord_x + i, cord_y, board):  # going upwards or downwards
            acc = follow_trail(cord_x + i, cord_y, board, current_height, acc)
        if is_in_bound(cord_x, cord_y + i, board):  # going left or right
            acc = follow_trail(cord_x, cord_y + i, board, current_height, acc)
    return acc

def count_trails_for_trailhead(cord_x, cord_y, board, acc):
    if board[cord_x][cord_y] != '0':
        raise Exception("Incorrect trailhead")
    for i in (-1,1):
        if is_in_bound(cord_x+i,cord_y, board): #going upwards or downwards
            acc = follow_trail(cord_x+i, cord_y, board, 0, acc)
        if is_in_bound(cord_x, cord_y+i, board): #going left or right
            acc = follow_trail(cord_x, cord_y+i, board, 0, acc)
    return acc

def solve_first(lines):
    acc = 0
    for x,l in enumerate(lines):
        for y,c in enumerate(l):
            if c == '0':
                acc = count_trails_for_trailhead(x,y,lines,acc)
    return acc

def solve_second(lines):
    pass


print(solve_first(parse()))
print(solve_second(parse()))