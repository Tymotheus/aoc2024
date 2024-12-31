def parse():
    return open("input_small.txt").read().splitlines()

def resolve(gate: str, inputs: dict):
    """Parse the gate string, look for the signal values of inputs in the input dict, then calculate the output value
        of the logical gate."""
    i1, i2, oper = gate[0:3], gate[-3:], gate[3:-3].strip()
    if i1 and i2 in inputs.keys():
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
    acc = 0
    inputs = dict()
    outputs = []
    gates = []
    # We prepare the dictionary that at the beginning holds values of initial input wires and will be expanded soon
    for i in range(len(lines)):
        if lines[i] == "":
            break
        else:
            x,y = lines[i].split(":")
            inputs[x] = int(y.strip())
    for i in range(i+1, len(lines)):
        x,y = lines[i].split("->")
        gates.append([x.strip(), y.strip()])

    for gate in gates: #This should be replaced with a while loop, iterating looking at the gates,
        # if some 2 inputs are known, calculates the output value and adds it to the inputs dictionary
        outputs.append([gate[1],resolve(gate[0], inputs)])
    print(outputs)

    # At the end, outputs should hold the values of the "zXXX" wires
    return acc


def solve_second(lines):
    acc = 0
    return acc


print(solve_first(parse()))
print(solve_second(parse()))