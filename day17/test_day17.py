import pytest
from day17 import read_input
from day17 import Computer

def test_read_input():
    registers, program = read_input("input1.txt")

    assert registers["A"] == 729
    assert registers["B"] == 0
    assert registers["C"] == 0

    assert program == [0,1,5,4,3,0]

@pytest.mark.parametrize("operand, expected", [
    (0, 0), (1,1), (2,2), (3,3), (4,17), (5,25), (6,7)
])
def test_combo(operand, expected):
    computer = Computer({'A':17, 'B': 25, 'C': 7})
    value = computer.combo(operand)

    assert value == expected

@pytest.mark.parametrize("numerator, denominator, expected", [
    (10, 2, 2), (11, 2, 2), (12, 2, 3), (13, 2, 3), 
    (32,5,1), (64,5,2)
])
def test_adv(numerator, denominator, expected):
    computer = Computer({'A':int(numerator), 'B': 5, 'C': 0})

    computer.execute_instr(0, denominator)
    actual = computer.A

    assert actual == expected
    assert computer.B == 5
    assert computer.C == 0

@pytest.mark.parametrize("numerator, denominator, expected", [
    (10, 2, 2), (11, 2, 2), (12, 2, 3), (13, 2, 3), 
    (32,5,1), (64,5,2)
])
def test_bdv(numerator, denominator, expected):
    computer = Computer({'A':int(numerator), 'B': 5, 'C': 0})

    computer.execute_instr(6, denominator)
    actual = computer.B

    assert actual == expected
    assert computer.C == 0

@pytest.mark.parametrize("numerator, denominator, expected", [
    (10, 2, 2), (11, 2, 2), (12, 2, 3), (13, 2, 3), 
    (32,5,1), (64,5,2)
])
def test_cdv(numerator, denominator, expected):
    computer = Computer({'A':int(numerator), 'B': 5, 'C': 0})

    computer.execute_instr(7, denominator)
    actual = computer.C

    assert actual == expected
    assert computer.B == 5



def test_execute_simple():
    registers, program = read_input("input1.txt")

    computer = Computer(registers)
    output = computer.execute(program)

    assert output == [4,6,3,5,6,3,5,2,1,0]
    print(",".join(map(str, output)))

