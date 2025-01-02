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
    acc = "".join(str(output[1]) for output in outputs) #We start appending with the most significant bit
    print(len(acc))
    return acc


def solve_second(lines):
    # How to sum 2 binary number?
    # We need to perform 2 operations: 1st summing the numbers - for that we use XOR. This is the "sum" result
    # 2nd we compute the "carry" (przeniesienie) with the and gate
    # At the end, we sum the next more significant bits + the carry
    inputs = dict()
    outputs = []
    gates = []
    acc = 0
    for i in range(len(lines)):
        if lines[i] == "":
            break
        else:
            x, y = lines[i].split(":")
            inputs[x] = int(y.strip())
    # How to find out if a wire is switched?
    # If the final output for a given z-bit is incorrect (downstream wires must have been switched)
    # If the final output bit is correct 0 downstream might have been switched (or not!)
    x, y = "", ""
    for i in reversed(range(int(len(inputs)/2))):
        s = f"0{i}" if i <10 else str(i)
        # acc+=("1" if (inputs[f"x{s}"] != inputs[f"y{s}"]==1) else "0")
        x+= str(inputs[f"x{s}"])
        y+= str(inputs[f"y{s}"])
    print(f"X: {int(x, 2)}")
    print(f"Y: {int(y, 2)}")
    #print("Z1: 1110101110010100010001001110110001010001110000") #Original output
    print("Z1: 1110101110010100010001010000110001010001110000")
    print(f"Z2: {'{0:b}'.format(int(x, 2)+int(y, 2))}")
    z1 = '1110101110010100010001001110110001010001110000'
    z2 = '{0:b}'.format(int(x, 2)+int(y, 2))
    for i in range(len(z1)):
        if z1[i] != z2[i]:
            print(abs(i-45))
            # After printing, turns out that at least 11 outputs are incorrect (going downstream)
            # X19 y19 is for sure incorrect. z19 should take into account third input (carry) and instead it is calculated using x19 and y19. (I think) this result should be instead upstream for z20 (carry)
            # ckt XOR jwg (ckt is xor for x20 y20)
            # jwg should be output of x19 AND y19
            # bnh OR sbg -> jwg ()
            # z-value should never be output of AND operation, always XOR of a sum and carry (EDIT: but there can be some extra operations before...)
    return acc


print(solve_first(parse()))
print(solve_second(parse()))