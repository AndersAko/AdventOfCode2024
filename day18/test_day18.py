from day18 import read_input, fall_bytes, map_to_str, find_shortest_path

def test_read_input():
    actual = read_input("input1.txt")

    assert actual == [(5,4),(4,2),(4,5),(3,0),(2,1),(6,3),(2,4),(1,5),(0,6),(3,3),(2,6),(5,1),
                      (1,2),(5,5),(2,5),(6,5),(1,4),(0,4),(6,4),(1,1),(6,1),(1,0),(0,5),(1,6),(2,0)]
    
def test_fall_12_bytes():
    bytes = read_input("input1.txt")
    map = set()
    fall_bytes(bytes, map, 12)

    assert map_to_str(map) == """...#...
..#..#.
....#..
...#..#
..#..#.
.#..#..
#.#...."""

def test_shortest_path_after_12():
    bytes = read_input("input1.txt")
    map = set()
    fall_bytes(bytes, map, 12)

    shortest = find_shortest_path(map, (0,0), (6,6))
    print(shortest)
    assert shortest == 22