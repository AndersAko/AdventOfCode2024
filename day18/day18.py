import os
from heapq import heappop, heappush

size = 71
filename = "input.txt"

def read_input(filename):
    cur_dir = os.path.dirname(__file__) 

    result = []
    with open(os.path.join(cur_dir, filename), "r") as in_file:
        for line in in_file:
            result.append(tuple(map(int, line.split(','))))
    return result

def fall(byte: tuple[int,int], map: set):
    map.add(byte)
    return map

def fall_bytes(bytes, map, number):
    for byte, num in zip(bytes, range(number)):
        fall(byte, map)

def map_to_str(map):
    lines = []
    for y in range(size):
        lines.append("".join('#' if (x,y) in map else '.' for x in range(size)))
    return "\n".join(lines)

def remain(x,y,end):
    x1, y1, = end
    return y1-y + x1 -x

def moves(map, state):
    x,y,p = state
    moves = []
    for dx, dy in [(0,-1), (1,0), (0,1), (-1,0)]:
        if x + dx >= 0 and x + dx < size and y + dy >= 0 and y + dy < size and (x+dx,y+dy) not in map:
            moves.append((x+dx,y+dy, p+1))
    return moves

def find_shortest_path(map, start, end):
    visited = {}
    search = []
    heappush(search, (0, *start, 0))
    while search:
        _, *state_to_check = heappop(search)
        # print(state_to_check)
        for next_state in moves(map, state_to_check):
            x,y,path = next_state
            if (x,y) == end:
                return path
            if (x,y) not in visited or path < visited[(x,y)]:
                visited[(x,y)] = path
                heappush(search, (path + remain(x,y,end), *next_state))
    print("No solution found")

def solve1(filename):
    num_bytes = 1024

    bytes = read_input(filename)
    map = set()
    fall_bytes(bytes, map, num_bytes)
    print(map_to_str(map))

    shortest = find_shortest_path(map, (0,0), (size-1,size-1))
    print(f"Part1: shortest path after {num_bytes} bytes is {shortest}")

def solve2(filename):
    bytes = read_input(filename)

    num_bytes = 1024
    while True:
        map = set()
        fall_bytes(bytes, map, num_bytes)
        print(map_to_str(map))

        shortest = find_shortest_path(map, (0,0), (size-1,size-1))
        if shortest is not None:
            print(f" {num_bytes} => {shortest}")
            num_bytes *= 2
        else:
            upper_limit = num_bytes
            lower_limit = num_bytes // 2
            break
    print(f" {upper_limit=}, {lower_limit=}")

    while upper_limit - lower_limit > 1:
        num_bytes = (upper_limit - lower_limit) // 2 + lower_limit
        map = set()
        fall_bytes(bytes, map, num_bytes)

        shortest = find_shortest_path(map, (0,0), (size-1,size-1))
        if shortest is not None:
            lower_limit = num_bytes
        else:
            upper_limit = num_bytes

    map = set()
    fall_bytes(bytes, map, lower_limit)
    shortest_at_lower = find_shortest_path(map, (0,0), (size-1,size-1))

    map = set()
    fall_bytes(bytes, map, upper_limit)
    shortest_at_upper = find_shortest_path(map, (0,0), (size-1,size-1))

    print(f" {lower_limit=} {shortest_at_lower}; {upper_limit=} {shortest_at_upper}")
    print(f"Part2: The block at {bytes[lower_limit]} blocks the exit")
if __name__ == "__main__":
    solve1(filename)
    solve2(filename)

