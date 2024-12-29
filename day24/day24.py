import os
import re
from math import log2

def read_input(filename):
    cur_dir = os.path.dirname(__file__)
    wires = {}
    gates = {}
    with open(os.path.join(cur_dir, filename), "r") as in_file:
        for line in in_file:
            if line == '\n': break
            wire, state = re.match("(\w+): (\d)", line).groups()
            wires[wire] = int(state)
        for line in in_file:
            in1, gate, in2, out = re.match("(\w+) (\w+) (\w+) -> (\w+)", line).groups()
            gates[out] = (gate, in1, in2)
    return wires, gates

def logic(gate, in1, in2, wires, gates, swapped):
    if gate == 'AND':
        return get_wire(in1, wires, gates, swapped) & get_wire(in2, wires, gates, swapped)
    if gate == 'XOR':
        return get_wire(in1, wires, gates, swapped) ^ get_wire(in2, wires, gates, swapped)
    if gate == 'OR':
        return get_wire(in1, wires, gates, swapped) | get_wire(in2, wires, gates, swapped)

def get_wire(wire, wires, gates, swapped):
    # swapped = {w1: w2, w2:w1, ... }
    if wire in swapped: wire = swapped[wire]
    if wire not in wires: 
        wires[wire] = logic(*gates[wire], wires, gates, swapped)
    return wires[wire]

def get_output(wires, gates, swapped):
    z_wires = sorted((w for w in gates.keys() if w.startswith('z')))
    output_value = 0
    digit = 1
    for z_wire in z_wires:
        value = get_wire(z_wire, wires, gates, swapped)
        output_value += value * digit
        digit *= 2
    return output_value

def trace_gate(gate, gates, exclude):
    if gate in gates and gate not in exclude:
        return [gate] + trace_gate(gates[gate][1], gates, exclude) + trace_gate(gates[gate][2], gates, exclude)
    return [gate]

def solve1(filename):
    wires, gates = read_input(filename)

    output_value = get_output(wires, gates, {})

    print(f"Part1: z-wires output {output_value}")
    return output_value

def solve2(filename):
    def swap(a,b):
        return {a:b, b:a}
    swapped = {} | swap('qjb', 'gvw') | swap('jgc', 'z15')| swap('drg', 'z22') | swap('jbp', 'z35')
    answer = ",".join(sorted(swapped.keys()))

    print (f"Part2: {answer}")


if __name__ == "__main__":
    filename = "input.txt"
    solve1(filename)
    solve2(filename)
