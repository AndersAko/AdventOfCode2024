from day23 import read_input, find_maximal_cliques, solve1, solve2
from math import factorial

def test_read_input():
    actual = read_input("input1.txt")

    assert 'cg' in actual['aq'] 
    assert 'yn' in actual['aq'] 
    assert 'aq' in actual['cg']
    
def test_maximal_cliques():
    graph = read_input("input1.txt")

    cliques = find_maximal_cliques(graph)
    three_node_cliques = sum( factorial(len(x)) / factorial(len(x)-3) / 6 for x in cliques if len(x) >= 3)
    assert three_node_cliques == 12

def test_solve1():
    result = solve1("input1.txt")

    assert result == 7

def test_solve2():
    result = solve2("input1.txt")

    assert result == "co,de,ka,ta"