from networkx.algorithms.approximation.clique import max_clique
import networkx as nx

def parse():
    return open("input.txt").read().splitlines()

def solve_first(lines):
    acc = 0
    parties = {}
    for line in lines:
        comps = line.split("-")
        if comps[0] in parties:
            parties[comps[0]].add(comps[1])
        else:
            parties[comps[0]] = {comps[1]}
        if comps[1] in parties:
            parties[comps[1]].add(comps[0])
        else:
            parties[comps[1]] = {comps[0]}
    solution = []
    for k, v in parties.items():
        if k[0] == 't':
            for i, node1 in enumerate(v):
                for node2 in v:
                    if node2 in parties[node1]:
                        if {k, node1, node2} not in solution:
                            solution.append({k, node1, node2})
                            acc+=1
    return acc


def solve_second(lines):
    acc = 0
    G = nx.Graph()
    G.add_edges_from([line.split("-") for line in lines])
    print(list(G.nodes))
    output = [i for i in nx.find_cliques(G)]
    max_len = 0
    max_clique = None
    for i in output:
        if len(i)>max_len:
            max_clique = i
            max_len = len(i)
    print(','.join(sorted(max_clique)))
    return acc


# print(solve_first(parse()))
print(solve_second(parse()))