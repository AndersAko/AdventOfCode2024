import pytest
from day22 import next_secret_gen, read_input, solve1, solve2

@pytest.mark.parametrize("secret, expected", [
    (123, 15887950), (15887950, 16495136), (16495136, 527345), (527345, 704524), (704524, 1553684),
    (1553684, 12683156), (12683156, 11100544), (11100544, 12249484), (12249484, 7753432), (7753432, 5908254)
])
def test_secret_sequence(secret, expected):
    gen = next_secret_gen(secret)
    actual = next(gen)

    assert actual == expected

def test_read_input():
    secrets = read_input("input1.txt")

    assert secrets == [1, 10, 100, 2024]

def test_solve1():
    result = solve1("input1.txt")

    assert result == 37327623

def test_solve2():
    result = solve2("input2.txt")
    assert result == 23

    