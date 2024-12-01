def parse():
    return open("input.txt").read().splitlines()


def solve_first(lines):
    acc = 0
    first_l = [int(i.split(' ')[0]) for i in lines]
    second_l = [int(i.split(' ')[-1]) for i in lines]
    first_l.sort()
    second_l.sort()
    for i in range(len(first_l)):
        acc += abs(first_l[i]-second_l[i])
    return acc


def solve_second(lines):
    acc = 0
    first_l = [int(i.split(' ')[0]) for i in lines]
    second_l = [int(i.split(' ')[-1]) for i in lines]
    first_l.sort()
    second_l.sort()
    for i in first_l:
        acc += i * second_l.count(i)
    return acc


print(solve_first(parse()))
print(solve_second(parse()))