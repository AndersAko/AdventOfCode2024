from day20 import read_input, find_shortest_path, solve1

def test_read_input():
    track, start, end = read_input("input1.txt")

    assert start == (1,3)
    assert end == (5,7)
    assert "\n".join(track) == """###############
#...#...#.....#
#.#.#.#.#.###.#
#.#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###...#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

def test_shortest_without_cheat():
    track, start, end = read_input("input1.txt")

    path_without_cheat = find_shortest_path(track, False, start, end)
    print(f"Shortest path without cheat: {path_without_cheat}")

    assert len(path_without_cheat) == 84 + 1

def test_solve1_sample_input():
    actual = solve1("input1.txt", 4)

    assert actual == 30