def parse():
    return open("input.txt").read().splitlines()


def solve_first(lines):
    acc = 0
    lockheights = []
    keyheights = []
    for j, i in enumerate(range(0, len(lines), 8)):
        print()
        lock = None
        if lines[i] == 5 * "#":
            # Locks have tops filled with hashes
            lock = True
            lockheights.append([-1 for _ in range(5)])
        elif lines[i + 6] == 5 * "#":
            lock = False  # Keys have bottoms filled with hashes
            keyheights.append([-1 for _ in range(5)])
        print(lock)
        for row in lines[i : i + 8]:
            for k, char in enumerate(row):
                if char == "#":
                    if lock:
                        lockheights[-1][k] += 1
                    elif not lock:
                        keyheights[-1][k] += 1
        print()
    print(keyheights)
    print(lockheights)
    for k in keyheights:
        for l in lockheights:
            ok = True
            for i in range(5):
                if k[i] + l[i] > 5:
                    ok = False
                    break
            if ok:
                acc += 1
    return acc


def solve_second(lines):
    acc = 0
    return acc


print(solve_first(parse()))
print(solve_second(parse()))
