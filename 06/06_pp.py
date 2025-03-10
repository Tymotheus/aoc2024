#Solution copied from Piotr Piątkowski

#!/usr/bin/python3

from tools import *
from copy import deepcopy
from collections import defaultdict

DMAP = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}
RROT = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}

debug = False

def dump(grid, pos, dir, path=None):
    W = max(x for x, y in grid.keys()) + 1
    H = max(y for x, y in grid.keys()) + 1

    path_dirs = defaultdict(set)
    path_syms = {}
    if path:
        for ppos, dir in path:
            path_dirs[ppos].add(dir)
        for k, ss in path_dirs.items():
            v = ''
            if '<' in ss or '>' in ss:
                v += '-'
            if '^' in ss or 'v' in ss:
                v += '|'
            if len(v) == 2:
                v = '+'
            path_syms[k] = v

    for y in range(H):
        for x in range(W):
            if (x,y) == pos:
                print(dir, end='')
            elif (x,y) in path_syms:
                print(path_syms[x,y], end='')
            else:
                print(grid[x,y], end='')
        print()


def has_loop(grid, pos, dir):
    path = {(pos,dir)}

    while pos in grid:
        dx, dy = DMAP[dir]
        npos = (pos[0]+dx, pos[1]+dy)
        while grid[npos] == '#':
            dir = RROT[dir]
            dx, dy = DMAP[dir]
            npos = (pos[0]+dx, pos[1]+dy)
        pos = npos
        if (pos, dir) in path:
            if (debug):
                print("LOOP")
                dump(grid, pos, dir, path)
            return True
        if grid[pos] == '':
            if (debug):
                print("NO LOOP")
                dump(grid, pos, dir, path)
            return False
        path.add((pos,dir))


def run(args):

    DIRS = list(DMAP.keys())

    lines = read_lines(args)

    grid = defaultdict(str)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x,y] = c
            if c in '^v<>':
                pos0 = (x,y)
                dir0 = c
                grid[x,y] = '.'

    pos = pos0
    dir = dir0

    path = {pos}

    while pos in grid:
        dx, dy = DMAP[dir]
        npos = (pos[0]+dx, pos[1]+dy)
        while grid[npos] == '#':
            dir = RROT[dir]
            dx, dy = DMAP[dir]
            npos = (pos[0]+dx, pos[1]+dy)
        pos = npos
        if grid[pos] == '':
            break
        path.add(pos)
        # dump(grid, pos, dir)
        # print()
        #input("ENTER")

    print(len(path))

    p2 = 0
    for npos in path:
        if grid[npos] == '.' and npos != pos0:
            grid[npos] = '#'
            if has_loop(grid, pos0, dir0):
                p2 += 1
                #print(f"loop for {npos}")
            grid[npos] = '.'

    print(p2)

main(run)