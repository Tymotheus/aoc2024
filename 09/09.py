
def parse():
    return open("input.txt").read()

def calc_checksum(table):
    acc = 0
    for i, c in enumerate(table):
        if c != -1:
           acc += c*i
    return acc

def copy_file_block(table, start_id, block_len):
    # Returns table after successfully copying, or the same table if copying is not possible.
    # We assume that empty blocks are represented by -1
    free_len = 0
    for id, char in enumerate(table[:start_id]): # We start going through the table from the left side, ending on the field that we start looking at
        if char == -1:
            free_len += 1
            if free_len == block_len:
                for i in range(id-block_len+1, id+1): # We recopy whole range to our newly found empty space
                    table[i] = table[start_id]
                for i in range(start_id, start_id + block_len): # We replace the old filespace with emptyspace
                    table[i] = -1
                return table
            continue
        else: #we are travelling through other fileblocks
            free_len = 0
    return table


def solve_first(line):
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
            new_format += [-1]*char #-1 represents empty spaces (dots in the riddle example)
            is_file = True
    while -1 in new_format:
        # We start moving the files from the end of line to first empty spaces from the left
        last_el = new_format[-1]
        new_format = new_format[:-1]
        if last_el == -1:
            continue
        for pos, c in enumerate(new_format):
            if c==-1:
                new_format[pos] = last_el
                break
    return calc_checksum(new_format)


def solve_second(line):
    file_id = 0
    max_copied = len(line) # prevents copying same fragments more than once
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
    pos = len(new_format)
    curr_file, block_len = None, 0
    while pos > 0:
        pos -= 1
        element = new_format[pos]
        if curr_file is not None and element == curr_file: # We continue going through fileblock
            block_len += 1
        elif curr_file is not None and element != curr_file: #End of file, time to try to move this file
            if curr_file < max_copied:
                new_format = copy_file_block(new_format, pos+1, block_len)
                max_copied = curr_file
            block_len = 0
            curr_file = None
            if element != -1:
                block_len, curr_file = 1, element
        elif element == -1 and curr_file is None: # We move through blocks of free space
            continue
        elif element != -1 and curr_file is None: # We encounter the first element of a new fileblock
            block_len = 1
            curr_file = new_format[pos]
            continue
    return calc_checksum(new_format)


print(solve_first(parse()))
print(solve_second(parse()))