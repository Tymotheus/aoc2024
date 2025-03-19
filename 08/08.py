from collections import defaultdict

def parse():
    return open("input.txt").read().splitlines()

def get_antinodes(a1_r, a1_c, a2_r, a2_c):
    # Returns row-column coordinates of antinodes 1 and 2
    # Basically simple vector calculations
    an_1_r = a1_r + a1_r - a2_r
    an_2_r = a2_r + a2_r - a1_r
    an_1_c = a1_c + a1_c - a2_c
    an_2_c = a2_c + a2_c - a1_c
    return (an_1_r, an_1_c), (an_2_r, an_2_c)

def add_resonant_antinodes(res_antinodes, a1_r, a1_c, a2_r, a2_c, R, C):
    # Adds antinodes position, for given antennas, to the set of antinodes
    # Move towards antenna 1, check how many antinodes fit within the grid
    # These are basically vector calculations
    i = j = 0
    an_1_r = a1_r + (i) * (a1_r - a2_r)
    an_1_c = a1_c + (i) * (a1_c - a2_c)
    while check_boundaries(an_1_r, an_1_c, R, C):
      res_antinodes.add((an_1_r, an_1_c))
      i+=1
      an_1_r = a1_r + (i) * (a1_r - a2_r)
      an_1_c = a1_c + (i) * (a1_c - a2_c)
    # Move towards antenna 2, check how many antinodes fit within the grid
    an_2_r = a2_r + (j) * (a2_r - a1_r)
    an_2_c = a2_c + (j) * (a2_c - a1_c)
    while check_boundaries(an_2_r, an_2_c, R, C):
        res_antinodes.add((an_2_r, an_2_c))
        j += 1
        an_2_r = a2_r + (j) * (a2_r - a1_r)
        an_2_c = a2_c + (j) * (a2_c - a1_c)
    return res_antinodes


def check_boundaries(r,c, R, C):
    # Check whether given position sits withing the given grid limits
    return R > r >= 0 and C > c >= 0

def solve(lines):
    acc1 = 0
    antennas = {}
    antinodes = set()
    res_antinodes = set() # Needed for part 2
    grid = defaultdict(str)
    for r, line in enumerate(lines):
        for c, field in enumerate(line):
            grid[r, c] = field
            if field != '.': # We gather positions of all antennas
                if field in antennas.keys():
                    antennas[field].append((r,c))
                else:
                    antennas[field] = [(r,c)]
    H = max(x for x,y in grid.keys()) + 1 # Height or number of rows
    W = max(y for x,y in grid.keys()) + 1 # Width or number of columns
    for typ, cords in antennas.items():
        l = len(cords)
        # We calculate antinodes for all antennas of the same type
        for a1 in range(l):
            for a2 in range(a1+1, l):
                for an in get_antinodes(*cords[a1], *cords[a2]):
                    if check_boundaries(an[0], an[1], W, H):
                        if an not in antinodes:
                            acc1 += 1
                            antinodes.add(an)
                res_antinodes = add_resonant_antinodes(res_antinodes, *cords[a1], *cords[a2], H, W)
    print(acc1)
    print(len(res_antinodes))


solve(parse())