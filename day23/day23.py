from collections import defaultdict
from math import factorial
from itertools import combinations
import os

def read_input(filename):
    cur_dir = os.path.dirname(__file__) 
    neighbors = defaultdict(set)
    with open(os.path.join(cur_dir, filename), "r") as in_file:
        for line in in_file:
            a, b = map(str.strip, line.split('-'))
            neighbors[a].add(b)
            neighbors[b].add(a)
    return dict(neighbors)

def find_maximal_cliques(graph):
    vertices = set(graph.keys())
    maximal_cliques = BronKerbosch(set(), vertices, set(), graph)
    return maximal_cliques

def BronKerbosch(R, P, X, graph) -> set[frozenset]:
    if len(P) == 0 and len(X) == 0:
        return { frozenset(R) }
    result = set()
    if len(P) > 0:
        u = max(P, key=lambda x: len(graph[x]))
        N_u = graph[u]
        for v in P - N_u:
            result |= BronKerbosch(R | {v}, P & graph[v], X & graph[v], graph)
            P = P - {v}
            X = X | {v}
    return result

def solve1(filename):
    graph = read_input(filename)

    cliques = find_maximal_cliques(graph)
    cliques_with_t = [ c for c in cliques if any(v.startswith('t') for v in c)]
    three_cliques_with_t = set()
    for clique in cliques_with_t:
        if len(clique) >= 3:
            cs = {c for c in combinations(sorted(clique), 3) if any(v.startswith('t') for v in c)}
            three_cliques_with_t.update(cs)
            # print (f"{clique}: {cs}")

    print(f"Part1: Networks including a 't'-node: {len(three_cliques_with_t)}")
    return len(three_cliques_with_t)

def solve2(filename):
    graph = read_input(filename)

    cliques = find_maximal_cliques(graph)
    maximum_clique = max(cliques, key=lambda c: len(c))
    password = ",".join(sorted(maximum_clique))
    print (f"Part2: Largest clique is {maximum_clique} => {password}")
    return password

if __name__ == "__main__":
    filename = "input.txt"
    solve1(filename)
    solve2(filename)
