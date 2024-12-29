import pytest
from math import log2
from day24 import read_input, logic, get_wire, solve1, get_output, trace_gate

def test_read_input():
    wires, gates = read_input("input2.txt")

    assert wires == {'x00': 1,'x01': 1,'x02': 1,'y00': 0,'y01': 1,'y02': 0}
    assert gates == {'z00': ('AND', 'x00', 'y00'),
                     'z01': ('XOR', 'x01', 'y01'),
                     'z02': ('OR', 'x02', 'y02') }

@pytest.mark.parametrize("gate, expected", [
    (('AND', 'x0', 'x0'), 0), (('AND', 'x1', 'x0'), 0), (('AND', 'x0', 'x1'), 0), (('AND', 'x1', 'x1'), 1),
    (('XOR', 'x0', 'x0'), 0), (('XOR', 'x1', 'x0'), 1), (('XOR', 'x0', 'x1'), 1), (('XOR', 'x1', 'x1'), 0),
    (('OR', 'x0', 'x0'), 0), (('OR', 'x1', 'x0'), 1), (('OR', 'x0', 'x1'), 1), (('OR', 'x1', 'x1'), 1)
])
def test_gates(gate, expected):
    wires = {'x0': 0, 'x1': 1}
    actual = logic(*gate, wires, {}, {})

    assert actual == expected

def test_gate_logic():
    wires, gates = read_input("input2.txt")

    z00 = get_wire('z00', wires, gates, {})
    z01 = get_wire('z01', wires, gates, {})
    z02 = get_wire('z02', wires, gates, {})

    assert z00 == 0
    assert z01 == 0
    assert z02 == 1

def test_solve1():
    result = solve1("input1.txt")

    assert result == 2024

@pytest.fixture
def adder():
    wires, gates = read_input("input.txt")
    return sorted(wires), gates

def swap(a,b):
    return {a:b, b:a}

@pytest.fixture
def swapped():
    return {} | swap('qjb', 'gvw') | swap('jgc', 'z15')| swap('drg', 'z22') | swap('jbp', 'z35')

def test_trace_gate():
    wires = {'x00': 1,'x01': 1,'x02': 1,'y00': 0,'y01': 1,'y02': 0}
    gates = {'z00': ('AND', 'x00', 'y00'),
             'z01': ('XOR', 'z00', 'y01'),
             'z02': ('OR', 'x02', 'z01') }

    result = trace_gate('z02', gates, set())
    assert sorted(result) == sorted(['z02', 'x02', 'z01', 'z00', 'y01', 'x00', 'y00'])

def test_trace_gate():
    wires = {'x00': 1,'x01': 1,'x02': 1,'y00': 0,'y01': 1,'y02': 0}
    gates = {'z00': ('AND', 'x00', 'y00'),
             'z01': ('XOR', 'z00', 'y01'),
             'z02': ('OR', 'x02', 'z01') }

    result = trace_gate('z02', gates, {'z00'})
    assert sorted(result) == sorted(['z02', 'x02', 'z01', 'z00', 'y01'])


def test_adder_zero_zero(adder, swapped):
    wires, gates = adder
    wires_zero = {w: 0 for w in wires}

    result = get_output(dict(wires_zero), gates, swapped)
    assert result == 0

@pytest.mark.parametrize("bit_no", range(45))
def test_adder_ones_in_x(adder, bit_no, swapped):
    wires, gates = adder
    wires = {w: 0 if w != f'x{bit_no:02}' else 1 for w in wires }

    result = get_output(wires, gates, swapped)
    assert result == 2 ** bit_no

@pytest.mark.parametrize("bit_no", range(45))
def test_adder_ones_in_y(adder, bit_no, swapped):
    wires, gates = adder
    wires = {w: 0 if w != f'y{bit_no:02}' else 1 for w in wires }

    result = get_output(wires, gates, swapped)
    print (result, bin(result))

    assert result == 2 ** bit_no

@pytest.mark.parametrize("bit_no", range(45))
def test_adder_carry(adder, bit_no, swapped):
    wires, gates = adder
    wires = {w: 0 if w != f'x{bit_no:02}' and w != f'y{bit_no:02}' else 1 for w in wires }

    result = get_output(wires, gates, swapped)
    print (result, bin(result))

    assert result == 2 ** (bit_no + 1)
