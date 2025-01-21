import pandas as pd
import numpy as np


def parse():
    return open("input.txt").read().splitlines()


def solve_first(lines):
    board = pd.DataFrame(list(line) for line in lines)
    acc = 0
    row_num = len(board)
    col_num = len(board[0])
    for r in range(row_num):
        for c in range(col_num):
            if r + 3 < row_num:  # XMAS appearing horizontally
                if board.iloc[r : r + 4, c].str.cat() in ("XMAS", "SAMX"):
                    acc += 1
            if c + 3 < col_num:  # XMAS appearing vertically
                if board.iloc[r, c : c + 4].str.cat() in ("XMAS", "SAMX"):
                    acc += 1
            if (
                r + 3 < row_num and c + 3 < col_num
            ):  # XMAS diagonally from top left to bottom right
                if pd.Series(np.diag(board.iloc[r : r + 4, c : c + 4])).str.cat() in (
                    "XMAS",
                    "SAMX",
                ):
                    acc += 1
            if (r + 3 < row_num) and (
                c - 3 > 0
            ):  # XMAS diagonally, top right to bottom left, except first column
                if pd.Series(
                    np.diag(board.iloc[r : r + 4, c : c - 4 : -1])
                ).str.cat() in ("XMAS", "SAMX"):
                    acc += 1
            if (
                (r + 3 < row_num) and (c - 3 == 0)
            ):  # ugly case, should be combined with the one above but I can not into slicing XD case only when the first column is involved
                if pd.Series(np.diag(board.iloc[r : r + 4, c::-1])).str.cat() in (
                    "XMAS",
                    "SAMX",
                ):
                    acc += 1
    return acc


def solve_second(lines):
    # Ditched calling the diagonal functions, for a longer conditional block
    board = pd.DataFrame(list(line) for line in lines)
    acc = 0
    row_num = len(board)
    col_num = len(board[0])
    for r in range(1, row_num - 1):
        for c in range(1, col_num - 1):
            if board.iloc[r, c] == "A":
                if (
                    (board.iloc[r - 1, c - 1] == "M")
                    and (board.iloc[r + 1, c + 1] == "S")
                ) or (
                    (board.iloc[r - 1, c - 1] == "S")
                    and (board.iloc[r + 1, c + 1] == "M")
                ):  # upper left to bottom right diagonal
                    if (
                        (board.iloc[r - 1, c + 1] == "M")
                        and (board.iloc[r + 1, c - 1] == "S")
                    ) or (
                        (board.iloc[r - 1, c + 1] == "S")
                        and (board.iloc[r + 1, c - 1] == "M")
                    ):
                        acc += 1
    return acc  # one accounting for field just before exiting the map


# print(solve_first(parse()))
print(solve_second(parse()))
