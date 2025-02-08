from collections import defaultdict

def parse():
    return open("input.txt").read().splitlines()

def get_antinodes(a1_r, a1_c, a2_r, a2_c):
    # Calculations to get positions of 2 potential antinodes
    # Antinode 1 and Antinode 2
    an_1_r = a1_r + a1_r - a2_r
    an_2_r = a2_r + a2_r - a1_r
    an_1_c = a1_c + a1_c - a2_c
    an_2_c = a2_c + a2_c - a1_c
    return (an_1_r, an_1_c), (an_2_r, an_2_c)

def add_resonant_antinodes(res_antinodes, a1_r, a1_c, a2_r, a2_c, R, C):
    # Move towards antenna 1
    i = j = 0
    stop = False
    while not stop:
        an_1_r = a1_r + (i) * (a1_r - a2_r)
        an_1_c = a1_c + (i) * (a1_c - a2_c)
        i+=1
        if not check_boundaries(an_1_r, an_1_c, R, C): stop = True
        else: res_antinodes.add((an_1_r, an_1_c))
        print(stop)
    # Move towards antenna 2
    stop = False
    while not stop:
        an_2_r = a2_r + (j) * (a2_r - a1_r)
        an_2_c = a2_c + (j) * (a2_c - a1_c)
        j += 1
        if not check_boundaries(an_2_r, an_2_c, R, C): stop = True
        else: res_antinodes.add((an_2_r, an_2_c))
        print(stop)
    return res_antinodes


def check_boundaries(r,c, R, C):
    return R > r >= 0 and C > c >= 0

def solve(lines):
    acc1 = 0
    antennas = {}
    antinodes = set()
    res_antinodes = set()
    grid = defaultdict(str)
    for r, line in enumerate(lines):
        for c, field in enumerate(line):
            grid[r, c] = field
            if field != '.': # We gather positions of all antennas
                if field in antennas.keys():
                    antennas[field].append((r,c))
                else:
                    antennas[field] = [(r,c)]
    H = max(x for x,y in grid.keys()) + 1
    W = max(y for x,y in grid.keys()) + 1
    print(antennas)
    print(grid)
    for typ, cords in antennas.items():
        l = len(cords)
        # We calculate antinodes for all antennas of the same type
        for a1 in range(l):
            for a2 in range(a1+1, l):
                print(a1, a2)
                for an in get_antinodes(*cords[a1], *cords[a2]):
                    if check_boundaries(an[0], an[1], W, H):
                        if an not in antinodes:
                            acc1 += 1
                            antinodes.add(an)
                res_antinodes = add_resonant_antinodes(res_antinodes, *cords[a1], *cords[a2], H, W)
    print(acc1)
    print(len(res_antinodes))


solve(parse())