from day16 import read_map, find_shortest_path

def test_part1_sample1():
    # Arrange
    map, start, end = read_map("input1.txt")

    # Act
    score, _ = find_shortest_path(map, start, end)

    assert score == 7036

def test_part1_sample2():
    # Arrange
    map, start, end = read_map("input2.txt")

    # Act
    score, _ = find_shortest_path(map, start, end)

    assert score == 11048

def test_part2_sample1():
    # Arrange
    map, start, end = read_map("input1.txt")

    # Act
    score, paths = find_shortest_path(map, start, end)

    good_tiles = { t for p in paths for t in p}
    assert len(good_tiles) == 45

def test_part2_sample2():
    # Arrange
    map, start, end = read_map("input2.txt")

    # Act
    score, paths = find_shortest_path(map, start, end)

    good_tiles = { t for p in paths for t in p}
    assert len(good_tiles) == 64
        