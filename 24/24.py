def parse():
    return open("input.txt").read().splitlines()

def resolve(gate: str, inputs: dict):
    """Parse the gate string, look for the signal values of inputs in the input dict, then calculate the output value
        of the logical gate."""
    i1, i2, oper = gate[0:3], gate[-3:], gate[3:-3].strip()
    if i1 in inputs.keys() and i2 in inputs.keys():
        i1 = inputs[i1]
        i2 = inputs[i2]
    else:
        return None
    if oper == "AND":
        return i1 & i2
    elif oper == "OR":
        return i1 | i2
    elif oper == "XOR":
        return i1 ^ i2
    else:
        return None

def solve_first(lines):
    inputs = dict()
    outputs = []
    gates = []
    # We prepare the dictionary that at the beginning holds values of initial input wires and will be expanded soon
    for i in range(len(lines)):
        if lines[i] == "": break
        else:
            x,y = lines[i].split(":")
            inputs[x] = int(y.strip())
    for i in range(i+1, len(lines)):
        x,y = lines[i].split("->")
        gates.append([x.strip(), y.strip()])
    while len(gates) > 0:
        gate = gates.pop(0)
        output = resolve(gate[0], inputs)
        if output is not None:
            inputs[gate[1]] = output
        else: gates.append(gate)
    # At the end, outputs should hold the values of the "zXXX" wires
    for i, j in inputs.items():
        if i[0] == 'z':
            outputs.append([i, j])
    outputs.sort(reverse=True)
    acc = int("".join(str(output[1]) for output in outputs), 2) #We start appending with the most significant bit
    return acc


def solve_second(lines):
    acc = ""
    inputs = dict()
    outputs = []
    gates = []
    for i in range(len(lines)):
        if lines[i] == "":
            break
        else:
            x, y = lines[i].split(":")
            inputs[x] = int(y.strip())
    for i in reversed(range(1, int(len(inputs)/2)),):
        s = f"0{i}" if i <10 else str(i)
        acc+=("1" if (inputs[f"x{s}"] == 1 and inputs[f"y{s}"]==1) else "0")
    return acc


print(solve_first(parse()))
print(solve_second(parse()))