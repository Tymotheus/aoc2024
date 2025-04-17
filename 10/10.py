def parse():
    return open("input.txt").read().splitlines()


def is_in_bound(cord_x, cord_y, board):
    if cord_x >= len(board) or cord_x < 0 or cord_y >= len(board[0]) or cord_y < 0:
        return False
    else:
        return True


def follow_trail(cord_x, cord_y, board, previous_height, trs, p_1):
    current_height = int(board[cord_x][cord_y])
    if current_height != previous_height + 1:  # Not a part of a good trail
        return trs
    elif board[cord_x][cord_y] == "9":
        if (cord_x, cord_y) in trs and p_1:
            return trs
        trs.append((cord_x, cord_y))
        return trs
    for i in (-1, 1):
        if is_in_bound(cord_x + i, cord_y, board):  # going upwards or downwards
            trs = follow_trail(cord_x + i, cord_y, board, current_height, trs, p_1)
        if is_in_bound(cord_x, cord_y + i, board):  # going left or right
            trs = follow_trail(cord_x, cord_y + i, board, current_height, trs, p_1)
    return trs


def count_trails_for_trailhead(cord_x, cord_y, board, p_1):
    if board[cord_x][cord_y] != "0":
        raise Exception("Incorrect trailhead")
    trs = []
    for i in (-1, 1):
        if is_in_bound(cord_x + i, cord_y, board):  # going upwards or downwards
            trs = follow_trail(cord_x + i, cord_y, board, 0, trs, p_1)
        if is_in_bound(cord_x, cord_y + i, board):  # going left or right
            trs = follow_trail(cord_x, cord_y + i, board, 0, trs, p_1)
    return len(trs)


def solve_first(lines):
    acc = 0
    for x, l in enumerate(lines):
        for y, c in enumerate(l):
            if c == "0":
                acc += count_trails_for_trailhead(x, y, lines, p_1=True)
    return acc


def solve_second(lines):
    acc = 0
    for x, l in enumerate(lines):
        for y, c in enumerate(l):
            if c == "0":
                acc += count_trails_for_trailhead(x, y, lines, p_1=False)
    return acc


print(solve_first(parse()))
print(solve_second(parse()))
