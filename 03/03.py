import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
pattern2  = r"mul\((\d{1,3}),(\d{1,3})\)|\b(do|don't)\(\)"



def parse():
    return open("input.txt").read()


def solve_first(lines):
    matches = re.findall(pattern, lines)

    print(matches)  # Output: [('123', '45'), ('9', '876')]
    sum=0
    for x,y in matches:
        sum+=int(x)*int(y)
    return sum


def solve_second(lines):
    matches = re.findall(pattern2, lines)
    result = []
    do = True
    sum = 0
    for match in matches:
        if match[0] and match[1]:  # It's a 'mul' match
            result.append((match[0], match[1]))
        elif match[2]:  # It's a 'do' or 'don't' match
            result.append(match[2])
    print(result)
    for i in result:
        if i == "do":
            do = True
        elif i == "don't":
            do = False
        elif do:
            sum += int(i[0]) * int(i[1])
    return sum


print(solve_first(parse()))
print(solve_second(parse()))