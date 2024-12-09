
def parse():
    return open("input_small.txt").read()

def solve_first(line):
    acc = 0
    file_id = 0
    new_format = []
    is_file = True #flag whether we now treat file or empty spaces
    line = [int(c) for c in line]
    for char in line:
        if is_file:
            new_format += [file_id]*char
            is_file = False
            file_id += 1
        else:
            new_format += [-1]*char
            is_file = True
    while -1 in new_format:
        last_el = new_format[-1]
        new_format = new_format[:-1]
        if last_el == -1:
            continue
        for pos, c in enumerate(new_format):
            if c==-1:
                new_format[pos] = last_el
                break
    for pos, c in enumerate(new_format):
        acc+= pos * c
    return acc


def solve_second(line):
    acc = 0
    file_id = 0
    new_format = []
    is_file = True  # flag whether we now treat file or empty spaces
    line = [int(c) for c in line]
    for char in line:
        if is_file:
            new_format += [file_id] * char
            is_file = False
            file_id += 1
        else:
            new_format += [-1] * char
            is_file = True
    print(new_format)
    stopping = False
    while not stopping:
        len = 0
        last_el = new_format[-1]
        for pos, num in enumerate(reversed(new_format)):
            if num == -1 and len > 0:
                for i in enumerate()
            if num == last_el:
                len += 1
        last_el = new_format[-1]
        new_format = new_format[:-1]
        if last_el == -1:
            continue
        if last_el == 0:
            stopping = True
        size = 0
        for c in reversed(new_format):
            if c == last_el:
                size+=1

        if c == 0: # we have traversed the whole list
            stopping = True
            continue



    return acc


# print(solve_first(parse()))
print(solve_second(parse()))