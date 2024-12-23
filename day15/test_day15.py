import pytest
from day15 import Warehouse, read_input, solve1, solve2

def test_push_left():
    warehouse = """#######
#...#.#
#.....#
#..OO.#
#..O..#
#.....#
#######
"""
    my_warehouse = list(map(list, warehouse.split('\n')))
    warehouse = Warehouse(my_warehouse, False)

    warehouse.push(5,3,-1,0)

    actual = warehouse.to_str()
    assert actual == """#######
#...#.#
#.....#
#.OO..#
#..O..#
#.....#
#######
"""

def test_push_up():
    warehouse = """#######
#...#.#
#.....#
#..OO.#
#..O..#
#.....#
#######
"""
    my_warehouse = list(map(list, warehouse.split('\n')))
    warehouse = Warehouse(my_warehouse, False)

    warehouse.push(3,5,0,-1)

    actual = warehouse.to_str()
    assert actual == """#######
#...#.#
#..O..#
#..OO.#
#.....#
#.....#
#######
"""

def test_push_up2():
    warehouse = """#######
#...#.#
#..O..#
#..OO.#
#..@..#
#..O..#
#######
"""
    my_warehouse = list(map(list, warehouse.split('\n')))
    warehouse = Warehouse(my_warehouse, False)

    warehouse.push(3,4,0,-1)

    actual = warehouse.to_str()
    assert actual == """#######
#..O#.#
#..O..#
#..@O.#
#.....#
#..O..#
#######
"""

def test_push_big_left_ok():
    warehouse = """##############
##......##..##
##...[][]...##
##....[]....##
##..........##
##..........##
##############
"""
    warehouse = Warehouse(map(list, warehouse.split('\n')), False)
    success = warehouse.push(9,2,-1,0)
    assert success
    actual = warehouse.to_str()
    assert actual == """##############
##......##..##
##..[][]....##
##....[]....##
##..........##
##..........##
##############
"""

def test_push_big_up_ok():
    warehouse = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##..........##
##############
"""
    warehouse = Warehouse(map(list, warehouse.split('\n')), False)

    success = warehouse.push(6,5,0,-1)

    assert success
    actual = warehouse.to_str()
    assert actual == """##############
##......##..##
##...[][]...##
##....[]....##
##..........##
##..........##
##############
"""

def test_push_big_up_nok():
    warehouse = """##############
##......##..##
##...[][]...##
##....[]....##
##..........##
##..........##
##############
"""
    warehouse = Warehouse(map(list, warehouse.split('\n')), False)
    success = warehouse.push(6,4,0,-1)
    assert not success
    actual = warehouse.to_str()
    assert actual == """##############
##......##..##
##...[][]...##
##....[]....##
##..........##
##..........##
##############
"""
def test_push_big_stack_down():
    warehouse = """####################
##[]..[]......[][]##
##[]...........[].##
##...........@[][]##
##..........[].[].##
##..##[]..[].[]...##
##...[]...[]..[]..##
##.....[]..[].[][]##
##........[]......##
####################"""
    warehouse = Warehouse(map(list, warehouse.split('\n')), False)
    success = warehouse.push(13,3,0,1)
    assert success
    actual = warehouse.to_str()
    assert actual == """####################
##[]..[]......[][]##
##[]...........[].##
##............[][]##
##...........@.[].##
##..##[]..[][]....##
##...[]...[].[]...##
##.....[]..[].[][]##
##........[]..[]..##
####################"""

def test_push_big_stack_down2():
    warehouse = """####################
##[]..[]......[][]##
##[]...........[].##
##............[][]##
##...........@.[].##
##..##[]..[][]....##
##...[]...[].[]...##
##.....[]..[].[][]##
##........[]......##
####################"""
    warehouse = Warehouse(map(list, warehouse.split('\n')), False)
    success = warehouse.push(13,4,0,1)
    assert success
    actual = warehouse.to_str()
    assert actual == """####################
##[]..[]......[][]##
##[]...........[].##
##............[][]##
##.............[].##
##..##[]..[].@....##
##...[]...[][]....##
##.....[]..[][].[]##
##........[]..[]..##
####################"""

def test_part1():
    wh, moves = read_input("input1.txt")
    actual = solve1(wh, moves)

    assert actual == 10092

def test_part2():
    wh, moves = read_input("input1.txt")
    actual = solve2(wh, moves)

    assert actual == 9021

def test_part2_simple():
    wh, moves = read_input("input2.txt")
    actual = solve2(wh, moves)

    assert actual == 618


